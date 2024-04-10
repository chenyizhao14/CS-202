import unittest
#from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_is_empty(self):
        q = Queue(10)
        self.assertTrue(q.is_empty)

    def test_queue_is_full(self):
        q = Queue(1)
        q.enqueue(10)
        self.assertTrue(q.is_full())

    def test_queue_enqueue_full(self):
        q = Queue(2)
        q.enqueue(5)
        q.enqueue(4)
        with self.assertRaises(IndexError):
            q.enqueue(20)

    def test_queue_dequeue_empty(self):
        q = Queue(3)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue_dequeue_return(self):
        q = Queue(3)
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(10, q.dequeue())
        q.enqueue(30)
        self.assertEqual(20, q.dequeue())

    def test_queue_size(self):
        q = Queue(2)
        q.enqueue(10)
        self.assertEqual(1, q.size())
        q.enqueue(20)
        self.assertEqual(2, q.size())

    def test_queue_circular_enqueue(self):
        q = Queue(3)
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.dequeue()
        q.enqueue(40)

    def test_queue_circular_dequeue(self):
        q = Queue(2)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.enqueue(4)
        q.dequeue()
        q.dequeue()




if __name__ == '__main__': 
    unittest.main()
