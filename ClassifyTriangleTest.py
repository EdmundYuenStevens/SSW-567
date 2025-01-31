import unittest
from ClassifyTriangle import classify_triangle

class TriangleTest(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(classify_triangle(0,0,0),"Invalid parameters, not a triangle")
        self.assertEqual(classify_triangle(1,1,10),"Invalid parameters, not a triangle")
        self.assertEqual(classify_triangle(-3,1,2),"Invalid parameters, not a triangle")
    def test_equilateral(self):
        self.assertEqual(classify_triangle(1,1,1),"Equilateral Triangle")
        self.assertEqual(classify_triangle(0.5,0.5,0.5),"Equilateral Triangle")
        self.assertEqual(classify_triangle(25,25,25),"Equilateral Triangle")
    def test_isosceles(self):
        self.assertEqual(classify_triangle(2,3,2),"Isosceles Triangle")
        self.assertEqual(classify_triangle(10,10,19),"Isosceles Triangle")
        self.assertEqual(classify_triangle(8,10,10),"Isosceles Triangle")
    def test_scalene(self):
        self.assertEqual(classify_triangle(4,5,6),"Scalene Triangle")
        self.assertEqual(classify_triangle(0.6,0.7,1.2),"Scalene Triangle")
        self.assertEqual(classify_triangle(2,4,5),"Scalene Triangle")
    def test_righttriangle(self):
        self.assertEqual(classify_triangle(3,4,5),"Right Triangle")
        self.assertEqual(classify_triangle(5,12,13),"Right Triangle")
        self.assertEqual(classify_triangle(8,15,17),"Right Triangle")

if __name__ == "__main__":
    unittest.main()