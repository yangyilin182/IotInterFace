import pytest
import time
def testcase_01():
    time.sleep(2)
    print('这里是testcase_01')
def testcase_02():
    time.sleep(4)
    print('这里是testcase_02')
def testcase_03():
    time.sleep(5)
    print('这里是testcase_03')
def testcase_04():
    time.sleep(9)
    print('这里是testcase_04')

if __name__ == "__main__":


    pytest.main(['-s', __file__, '-n=2'])
    #pytest.main(['-s', __file__,'--workers=2','--tests-per-worker=2'])