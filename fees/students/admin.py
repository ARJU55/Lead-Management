from django.contrib import admin
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal_Info', {
            'fields': ['student_name', 'gender', 'email', 'alternative_email', 'address',
                       'alternative_address', 'dob', 'mobile', 'street', 'pincodes', 'whatsapp'],
            'classes': ['wide'],
        }),
        
        ('Academic_Info', {
            'fields': ['college_Name', 'year_of_pass','roll_no','registration_number'], 
            'classes': ['wide'],
        }),
        ('Photos', {
            'fields': ['photo'], 
            'classes': ['wide'],
        }),
                ('GENERAL', {
            'fields': ['Enquirysource'], 
            'classes': ['wide'],
        }),
            
                ('PhoneVerifications', {
            'fields': ['phone'], 
            'classes': ['wide'],
            
        }),
                            
                ('COURSE_INFO', {
            'fields': ['COURSE'], 
            'classes': ['wide'],
            
        }),
    ]


    # Other fields and configurations here...

    

    




admin.site.register(Students, StudentsAdmin)

