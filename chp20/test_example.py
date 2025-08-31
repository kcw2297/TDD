from abc import abstractmethod

class TestCase:
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def setUp(self):
        pass
    
    @abstractmethod
    def tearDown(self):
        pass 
        
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
        
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "
        
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod"

    def tearDown(self):
        self.log = self.log + "tearDown"
    
        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")    

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
        
    def testSetUp(self):
        self.test.run()
        assert ("setUp testMethod" == self.test.log)
        
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown" == test.log)
        
TestCaseTest('setUp').run()
