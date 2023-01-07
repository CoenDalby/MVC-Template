from MVC.models import modeltemplate
from MVC.views import viewtemplate

class Controller:

    def __init__(self):
        #Model is where controller 
        #gets data to use in methods.
        self.model = modeltemplate.Model()
        #Controller passes itself to view
        #so view can use its function.
        self.view = viewtemplate.View(self)
        return


    #This is the function called by
    #main that starts the program flow.
    def primary_function(self):
        self.view.display_options()
        return

    #When the view needs data, it
    #gets it from controller, which
    #gets it from model. Anything
    #that needs to be done to the data
    #before it can be displayed by view
    #is handled by the controller.
    def get_data_alpha(self):
        data = self.model.get_data()
        data = "alpha "+data
        return(data)

    def get_data_beta(self):
        data = self.model.get_data()
        data = "beta "+data
        return(data)


        