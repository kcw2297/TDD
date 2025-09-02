from abc import abstractmethod


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
        
    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"

class TestCase:
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def setUp(self):
        pass
    
    @abstractmethod
    def tearDown(self):
        pass 
        
    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

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
    
    def testBrokenMethod(self):
        raise Exception
    
        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")    

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

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
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
        
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
        
        
TestCaseTest('testResult').run()
