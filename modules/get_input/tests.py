from django.test import TestCase
from django.test import Client
from django.urls import reverse

# Create your tests here.

from get_input.views import DiseaseEntryForm

class DiseaseTrendsTests(TestCase):

    def test_page_renders(self):
        
        client = Client()
        response = client.get(reverse('get_input:get_input'))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, "<h1>Disease trends</h1>")

    def test_valid_data_passes(self):
        
        form = DiseaseEntryForm({
            'name'      : "autism",
            'start_year': "2005",
            'end_year'  : "2010",
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data_fails(self):
        
        form = DiseaseEntryForm({
            'name'      : "autism",
            'start_year': "2010",
            'end_year'  : "2005",
        })
        self.assertFalse(form.is_valid())

        form = DiseaseEntryForm({
            'name'      : "autism",
            'start_year': "not an integer",
            'end_year'  : "2005",
        })
        self.assertFalse(form.is_valid())

        form = DiseaseEntryForm({
            'name'      : "autism",
            'start_year': "2004",
            'end_year'  : "not an integer",
        })
        self.assertFalse(form.is_valid())

        form = DiseaseEntryForm({
            'name'      : "autism",
            'start_year': "2010",
            'end_year'  : "2030",
        })
        self.assertFalse(form.is_valid())

        form = DiseaseEntryForm({
            'name'      : "",
            'start_year': "2010",
            'end_year'  : "2030",
        })
        self.assertFalse(form.is_valid())

