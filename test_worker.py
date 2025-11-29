import unittest
from worker import WORKER
from datetime import datetime

class TestWORKER(unittest.TestCase):
    def setUp(self):
        self.worker = WORKER("Иванов И.И.", "Инженер", 50000, 2018)

    def test_initialization(self):
        self.assertEqual(self.worker.get_surname(), "Иванов И.И.")
        self.assertEqual(self.worker.get_position(), "Инженер")
        self.assertEqual(self.worker.get_salary(), 50000)
        self.assertEqual(self.worker.get_year_joined(), 2018)

    def test_set_methods(self):
        self.worker.set_surname("Петров П.П.")
        self.assertEqual(self.worker.get_surname(), "Петров П.П.")

        self.worker.set_position("Менеджер")
        self.assertEqual(self.worker.get_position(), "Менеджер")

        self.worker.set_salary(60000)
        self.assertEqual(self.worker.get_salary(), 60000)

        self.worker.set_year_joined(2020)
        self.assertEqual(self.worker.get_year_joined(), 2020)

    def test_get_experience(self):
        current_year = datetime.now().year
        expected_experience = current_year - 2018
        self.assertEqual(self.worker.get_experience(), expected_experience)

    def test_experience_filter(self):
        workers = [
            self.worker,
            WORKER("Сидоров С.С.", "Разработчик", 45000, 2022),
        ]
        min_experience = 3
        filtered = [w for w in workers if w.get_experience() > min_experience]
        self.assertIn(self.worker, filtered)
        self.assertNotIn(workers[1], filtered)

if __name__ == "__main__":
    unittest.main()