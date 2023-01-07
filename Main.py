from MVC import controller


class Main:    
    @staticmethod
    def run():
        #Main creates a controller object,
        #and then tells it to execute one
        #of its methods.
        mainController = controller.Controller()
        mainController.primary_function()
        return



if __name__ == "__main__":
    Main.run()