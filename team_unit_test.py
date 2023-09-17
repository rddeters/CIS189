import unittest
from final_definitions.volleyball_definitions import Team as t
from final_definitions.volleyball_definitions import InvalidSchoolException as s
from final_definitions.volleyball_definitions import InvalidLocationException as l

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.team = t('ISU', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0)

    def tearDown(self):
        del self.team

    def test_object_created_all_attributes(self):
        self.assertEqual(self.team.school_acronym, 'ISU')
        self.assertEqual(self.team.team_school, 'Iowa State University')
        self.assertEqual(self.team.team_mascot, 'Cyclones')
        self.assertEqual(self.team.team_city, 'Ames')
        self.assertEqual(self.team.team_state, 'IA')
        self.assertEqual(self.team.num_wins, 3)
        self.assertEqual(self.team.num_losses, 0)

    def test_student_str(self):
        self.assertEqual(str(self.team.__str__()), 'The ISU volleyball team from Iowa State University, known as the Cyclones, from Ames, IA has 3 wins and 0 losses so far this season.')

    def test_student_record(self):
        self.assertEqual(str(self.team.print_record()), 'The record for Iowa State University is: (3, 0)')

    def test_team_cheer(self):
        self.assertEqual(str(self.team.team_cheer()), 'Go ISU Cyclones!')

    def test_object_not_created_error_abbreviation(self):
        with self.assertRaises(s):
            p = t('$', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0)

    def test_object_not_created_error_school_name(self):
        with self.assertRaises(s):
            p = t('ISU', '$', 'Cyclones', 'Ames', 'IA', 3, 0)

    def test_object_not_created_error_mascot(self):
        with self.assertRaises(s):
            p = t('ISU', 'Iowa State University', '$', 'Ames', 'IA', 3, 0)

    def test_object_not_created_error_city(self):
        with self.assertRaises(l):
            p = t('ISU', 'Iowa State University', 'Cyclones', '$', 'IA', 3, 0)

    def test_object_not_created_error_state(self):
        with self.assertRaises(l):
            p = t('ISU', 'Iowa State University', 'Cyclones', 'Ames', '$', 3, 0)


if __name__ == '__main__':
    unittest.main()
