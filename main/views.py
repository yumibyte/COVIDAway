from django.shortcuts import render
from django.utils import timezone
from django.views import View
from main.models import Individual

# Create your views here.

class MainView(View):
    url = ""
    #Establish a dictionary that will be sent to the template html
    #context = { }

    #Used to render a page
    def load_page(self, request, page, context = {}):
        print("New webpage request (" + page + ")")
        return render(request, page, context)

    def check_sub(self, submission):
        #SUBMISSION DICTIONARY - name, email, people, need_gloves, need_faceshields, need_facemasks, notes
        print("Checking...")
        #if submission['lat'] is not "" and submission['long'] is not "":
            #print("Coords passed")
        if submission['name'].replace(" ", "").isalpha() and len(submission['name']) < 255:
            print("Name passed")
            if submission['email'].replace("@", "").replace(".","").isalnum() and "@" in submission['email'] and "." in submission['email'].split("@")[1] and len(submission['email']) < 255:
                print("Email passed")
                if submission['people'].isdigit() and int(submission['people']) in range(1, 10000): #people must be < 10,000
                    print("People passed")
                    if 'need_gloves' not in submission or 'need_faceshields' not in submission or 'need_facemasks' not in submission:
                        print("PPE passed")
                        if len(submission['notes']) < 5000:
                            print("Notes passed")
                            self.write_individual(submission)
                            return True
        return False

    def write_individual(self, submission):
        i = Individual(name=submission['name'], email=submission['email'], people=int(submission['people']), lat=float(submission['lat']), long=float(submission['long']), time=timezone.now())

        if 'need_gloves' in submission:
            i.need_gloves = True
        if 'need_faceshields' in submission:
            i.need_faceshields = True
        if 'need_facemasks' in submission:
            i.need_facemasks = True
        if len(submission['notes']) > 0:
            i.notes = submission['notes']

        i.save()
        
    def write_distributor(self, submission):
        d = Distributor(name=submission['name'], website=submission['website'], nomasks=int(submission['nomasks']), noshields=int(submissions['noshields']), nogloves=int(submissions['nogloves']), lat=float(submission['lat']), long=float(submission['long']))

    #When a user goes to the page without posting data
    def get(self, request):
        if self.url == "donateppe":
            return self.load_page(request, 'donateppe.html')
        else:
            return self.load_page(request, 'requestppe.html')

    #When the user posts data to the server
    def post(self, request):
        print("-----")
        print(request.POST)
        print("-----")

        text = "Whoops! Something's gone wrong!"
        if self.check_sub(request.POST):
            text = "Your information has been submitted successfully!"

        return self.load_page(request, 'result.html', {'text': text})



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