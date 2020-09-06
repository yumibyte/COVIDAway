from django.shortcuts import render
from django.views import View

# Create your views here.

class MainView(View):
    #Establish a dictionary that will be sent to the template html
    context = { }

    #Used to render a page
    def load_page(self, request, page):
        print("New webpage request (" + page + ")")
        return render(request, page, self.context)

    #When a user goes to the page without posting data
    def get(self, request):
        return self.load_page(request, 'requestppe.html')

'''
    #When a user goes to the page without posting data
    def get(self, request):
        self.update_context()
        return self.load_page(request, 'bugtracker.html')
    
    #When the user posts data to the server
    def post(self, request):
        self.update_context()
        #Create a variable to represent each form that may have been filled out (Submiting a bug or changing its status)
        bug_report = SubmitBugForm(request.POST)
        status_change = ChangeStatusForm(request.POST)
        #If the user is submitting a bug report call the validation definition and set the context variables to match the response
        if bug_report.is_valid():
            self.context['error'], self.context['error_msg'], self.context['form'] = self.validate_bug_report(bug_report)
        #If the user is submitting a status change
        elif status_change.is_valid():
            self.validate_status_change(status_change)
        return self.load_page(request, 'bugtracker.html')
'''