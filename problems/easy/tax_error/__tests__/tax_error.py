import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tax_error import calculate_tax

testcase = [10000,0,-500]
expected = [1500,0.0,"Income can't be negative"]
def test():
    passed = True
    for x in range(3):
        if calculate_tax(testcase[x]) != expected[x]:
            passed = False
            print(f"❌ python text {x} failed")
            break
    
    print("✅ Python test passed!")

if __name__ =="__main__":
    test()