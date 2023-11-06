class Singleton:
    def __new__(cls):
        """
        Create and return a singleton instance of the class.

        This method is called when an instance of the class is created. It checks if the class
        already has an instance. If it does, it returns the existing instance. If it doesn't,
        it creates a new instance and calls the setup method.

        Parameters:
            cls (class): The class object.

        Returns:
            object: The singleton instance of the class.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.setup()
        return cls.instance

    def setup():
        pass