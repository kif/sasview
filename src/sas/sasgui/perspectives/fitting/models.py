"""
    Utilities to manage models
"""
import wx
import imp
import os
import sys
import math
import os.path
# Time is needed by the log method
import time
import logging
import py_compile
import shutil
from sas.sasgui.guiframe.events import StatusEvent
# Explicitly import from the pluginmodel module so that py2exe
# places it in the distribution. The Model1DPlugin class is used
# as the base class of plug-in models.
from sas.models.pluginmodel import Model1DPlugin
from sas.models.BaseComponent import BaseComponent
from sas.sasgui.guiframe.CategoryInstaller import CategoryInstaller
from sasmodels.sasview_model import make_class
import sasmodels.core


PLUGIN_DIR = 'plugin_models'

def get_model_python_path():
    """
        Returns the python path for a model
    """
    return os.path.dirname(__file__)


def log(message):
    """
        Log a message in a file located in the user's home directory
    """
    dir = os.path.join(os.path.expanduser("~"), '.sasview', PLUGIN_DIR)
    out = open(os.path.join(dir, "plugins.log"), 'a')
    out.write("%10g:  %s\n" % (time.clock(), message))
    out.close()


def _check_plugin(model, name):
    """
    Do some checking before model adding plugins in the list

    :param model: class model to add into the plugin list
    :param name:name of the module plugin

    :return model: model if valid model or None if not valid

    """
    #Check if the plugin is of type Model1DPlugin
    if not issubclass(model, Model1DPlugin):
        msg = "Plugin %s must be of type Model1DPlugin \n" % str(name)
        log(msg)
        return None
    if model.__name__ != "Model":
        msg = "Plugin %s class name must be Model \n" % str(name)
        log(msg)
        return None
    try:
        new_instance = model()
    except:
        msg = "Plugin %s error in __init__ \n\t: %s %s\n" % (str(name),
                                                             str(sys.exc_type),
                                                             sys.exc_info()[1])
        log(msg)
        return None

    if hasattr(new_instance, "function"):
        try:
            value = new_instance.function()
        except:
            msg = "Plugin %s: error writing function \n\t :%s %s\n " % \
                    (str(name), str(sys.exc_type), sys.exc_info()[1])
            log(msg)
            return None
    else:
        msg = "Plugin  %s needs a method called function \n" % str(name)
        log(msg)
        return None
    return model


def find_plugins_dir():
    """
        Find path of the plugins directory.
        The plugin directory is located in the user's home directory.
    """
    dir = os.path.join(os.path.expanduser("~"), '.sasview', PLUGIN_DIR)

    # If the plugin directory doesn't exist, create it
    if not os.path.isdir(dir):
        os.makedirs(dir)

    # Find paths needed
    try:
        # For source
        if os.path.isdir(os.path.dirname(__file__)):
            p_dir = os.path.join(os.path.dirname(__file__), PLUGIN_DIR)
        else:
            raise
    except:
        # Check for data path next to exe/zip file.
        #Look for maximum n_dir up of the current dir to find plugins dir
        n_dir = 12
        p_dir = None
        f_dir = os.path.join(os.path.dirname(__file__))
        for i in range(n_dir):
            if i > 1:
                f_dir, _ = os.path.split(f_dir)
            plugin_path = os.path.join(f_dir, PLUGIN_DIR)
            if os.path.isdir(plugin_path):
                p_dir = plugin_path
                break
        if not p_dir:
            raise
    # Place example user models as needed
    if os.path.isdir(p_dir):
        for file in os.listdir(p_dir):
            file_path = os.path.join(p_dir, file)
            if os.path.isfile(file_path):
                if file.split(".")[-1] == 'py' and\
                    file.split(".")[0] != '__init__':
                    if not os.path.isfile(os.path.join(dir, file)):
                        shutil.copy(file_path, dir)

    return dir


class ReportProblem:
    """
        Class to check for problems with specific values
    """
    def __nonzero__(self):
        type, value, traceback = sys.exc_info()
        if type is not None and issubclass(type, py_compile.PyCompileError):
            print "Problem with", repr(value)
            raise type, value, traceback
        return 1

report_problem = ReportProblem()


def compile_file(dir):
    """
    Compile a py file
    """
    try:
        import compileall
        compileall.compile_dir(dir=dir, ddir=dir, force=1,
                               quiet=report_problem)
    except:
        return sys.exc_info()[1]
    return None


def _findModels(dir):
    """
    """
    # List of plugin objects
    plugins = {}
    dir = find_plugins_dir()
    # Go through files in plug-in directory
    #always recompile the folder plugin
    if not os.path.isdir(dir):
        msg = "SasView couldn't locate Model plugin folder."
        msg += """ "%s" does not exist""" % dir
        logging.warning(msg)
        return plugins
    else:
        log("looking for models in: %s" % str(dir))
        compile_file(dir)
        logging.info("plugin model dir: %s" % str(dir))
    try:
        list = os.listdir(dir)
        for item in list:
            toks = os.path.splitext(os.path.basename(item))
            if toks[1] == '.py' and not toks[0] == '__init__':
                name = toks[0]

                path = [os.path.abspath(dir)]
                file = None
                try:
                    (file, path, info) = imp.find_module(name, path)
                    module = imp.load_module(name, file, item, info)
                    if hasattr(module, "Model"):
                        try:
                            if _check_plugin(module.Model, name) != None:
                                plugins[name] = module.Model
                        except:
                            msg = "Error accessing Model"
                            msg += "in %s\n  %s %s\n" % (name,
                                                         str(sys.exc_type),
                                                         sys.exc_info()[1])
                            log(msg)
                except:
                    msg = "Error accessing Model"
                    msg += " in %s\n  %s %s \n" % (name,
                                                   str(sys.exc_type),
                                                   sys.exc_info()[1])
                    log(msg)
                finally:

                    if not file == None:
                        file.close()
    except:
        # Don't deal with bad plug-in imports. Just skip.
        msg = "Could not import model plugin: %s" % sys.exc_info()[1]
        log(msg)
    return plugins


class ModelList(object):
    """
    Contains dictionary of model and their type
    """
    def __init__(self):
        """
        """
        self.mydict = {}

    def set_list(self, name, mylist):
        """
        :param name: the type of the list
        :param mylist: the list to add

        """
        if name not in self.mydict.keys():
            self.reset_list(name, mylist)

    def reset_list(self, name, mylist):
        """
        :param name: the type of the list
        :param mylist: the list to add
        """
        self.mydict[name] = mylist

    def get_list(self):
        """
        return all the list stored in a dictionary object
        """
        return self.mydict


class ModelManagerBase:
    """
        Base class for the model manager
    """
    ## external dict for models
    model_combobox = ModelList()
    ## Dictionary of form factor models
    form_factor_dict = {}
    ## dictionary of structure factor models
    struct_factor_dict = {}
    ##list of structure factors
    struct_list = []
    ##list of model allowing multiplication by a structure factor
    multiplication_factor = []
    ##list of multifunctional shapes (i.e. that have user defined number of levels
    multi_func_list = []
    ## list of added models -- currently python models found in the plugin dir.
    plugins = []
    ## Event owner (guiframe)
    event_owner = None
    last_time_dir_modified = 0

    def __init__(self):
        """
        """
        self.model_dictionary = {}
        self.stored_plugins = {}
        self._getModelList()

    def findModels(self):
        """
        find  plugin model in directory of plugin .recompile all file
        in the directory if file were modified
        """
        temp = {}
        if self.is_changed():
            return  _findModels(dir)
        logging.info("plugin model : %s" % str(temp))
        return temp

    def _getModelList(self):
        """
        List of models we want to make available by default
        for this application

        :return: the next free event ID following the new menu events

        """

        # regular model names only
        base_message = "Unable to load model {0}"
        self.model_name_list = []

        #Build list automagically from sasmodels package
        for mod_name in sasmodels.core.list_models():
            try:
                mod_def = sasmodels.core.load_model_info(mod_name)
                self.model_dictionary[mod_def['name']] = make_class(mod_def,dtype=None,namestyle='name')
                if mod_def['structure_factor'] == True:
                    self.struct_list.append(self.model_dictionary[mod_def['name']])
                if mod_def['variant_info'] is not None:
                    self.multi_func_list.append(self.model_dictionary[mod_def['name']])
                else:
                    self.model_name_list.append(mod_def['name'])
                if mod_def['ER'] is not None:
                    self.multiplication_factor.append(self.model_dictionary[mod_def['name']])
            except:
                logging.info("Problem loading %s model" % mod_name)

        #Looking for plugins
        self.stored_plugins = self.findModels()
        self.plugins = self.stored_plugins.values()
        for name, plug in self.stored_plugins.iteritems():
            self.model_dictionary[name] = plug

        self._get_multifunc_models()

        return 0

    def is_changed(self):
        """
        check the last time the plugin dir has changed and return true
         is the directory was modified else return false
        """
        is_modified = False
        plugin_dir = find_plugins_dir()
        if os.path.isdir(plugin_dir):
            temp = os.path.getmtime(plugin_dir)
            if  self.last_time_dir_modified != temp:
                is_modified = True
                self.last_time_dir_modified = temp

        return is_modified

    def update(self):
        """
        return a dictionary of model if
        new models were added else return empty dictionary
        """
        new_plugins = self.findModels()
        if len(new_plugins) > 0:
            for name, plug in  new_plugins.iteritems():
                if name not in self.stored_plugins.keys():
                    self.stored_plugins[name] = plug
                    self.plugins.append(plug)
                    self.model_dictionary[name] = plug
            self.model_combobox.set_list("Customized Models", self.plugins)
            return self.model_combobox.get_list()
        else:
            return {}

    def plugins_reset(self):
        """
        return a dictionary of model
        """
        self.plugins = []
        new_plugins = _findModels(dir)
        for name, plug in  new_plugins.iteritems():
            for stored_name, stored_plug in self.stored_plugins.iteritems():
                if name == stored_name:
                    del self.stored_plugins[name]
                    del self.model_dictionary[name]
                    break
            self.stored_plugins[name] = plug
            self.plugins.append(plug)
            self.model_dictionary[name] = plug

        self.model_combobox.reset_list("Customized Models", self.plugins)
        return self.model_combobox.get_list()

    def _on_model(self, evt):
        """
        React to a model menu event

        :param event: wx menu event

        """
        if int(evt.GetId()) in self.form_factor_dict.keys():
            from sas.models.MultiplicationModel import MultiplicationModel
            self.model_dictionary[MultiplicationModel.__name__] = MultiplicationModel
            model1, model2 = self.form_factor_dict[int(evt.GetId())]
            model = MultiplicationModel(model1, model2)
        else:
            model = self.struct_factor_dict[str(evt.GetId())]()


    def _get_multifunc_models(self):
        """
        Get the multifunctional models
        """
        for item in self.plugins:
            try:
                # check the multiplicity if any
                if item.multiplicity_info[0] > 1:
                    self.multi_func_list.append(item)
            except:
                # pass to other items
                pass

    def get_model_list(self):
        """
        return dictionary of models for fitpanel use

        """
        ## Model_list now only contains attribute lists not category list.
        ## Eventually this should be in one master list -- read in category
        ## list then pull those models that exist and get attributes then add
        ## to list ..and if model does not exist remove from list as now
        ## and update json file.
        ##
        ## -PDB   April 26, 2014

#        self.model_combobox.set_list("Shapes", self.shape_list)
#        self.model_combobox.set_list("Shape-Independent",
#                                     self.shape_indep_list)
        self.model_combobox.set_list("Structure Factors", self.struct_list)
        self.model_combobox.set_list("Customized Models", self.plugins)
        self.model_combobox.set_list("P(Q)*S(Q)", self.multiplication_factor)
        self.model_combobox.set_list("multiplication",
                                     self.multiplication_factor)
        self.model_combobox.set_list("Multi-Functions", self.multi_func_list)
        return self.model_combobox.get_list()

    def get_model_name_list(self):
        """
        return regular model name list
        """
        return self.model_name_list

    def get_model_dictionary(self):
        """
        return dictionary linking model names to objects
        """
        return self.model_dictionary


class ModelManager(object):
    """
    implement model
    """
    __modelmanager = ModelManagerBase()
    cat_model_list = [model_name for model_name \
                      in __modelmanager.model_dictionary.keys() \
                      if model_name not in __modelmanager.stored_plugins.keys()]

    CategoryInstaller.check_install(model_list=cat_model_list)
    def findModels(self):
        return self.__modelmanager.findModels()

    def _getModelList(self):
        return self.__modelmanager._getModelList()

    def is_changed(self):
        return self.__modelmanager.is_changed()

    def update(self):
        return self.__modelmanager.update()

    def plugins_reset(self):
        return self.__modelmanager.plugins_reset()

    def populate_menu(self, modelmenu, event_owner):
        return self.__modelmanager.populate_menu(modelmenu, event_owner)

    def _on_model(self, evt):
        return self.__modelmanager._on_model(evt)

    def _get_multifunc_models(self):
        return self.__modelmanager._get_multifunc_models()

    def get_model_list(self):
        return self.__modelmanager.get_model_list()

    def get_model_name_list(self):
        return self.__modelmanager.get_model_name_list()

    def get_model_dictionary(self):
        return self.__modelmanager.get_model_dictionary()
