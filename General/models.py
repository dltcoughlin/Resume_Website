from django.db import models

class Skill_Parent(models.Model):
    Skill_Parent_Name = models.CharField(max_length = 200)
    def __str__(self):
       return self.Skill_Parent_Name

class Source_Type(models.Model):
    Source_Type = models.CharField(max_length = 200)
    def __str__(self):
       return self.Source_Type
       
class Education(models.Model):
    School_Name = models.CharField(max_length = 200, default = None)
    Start_Year = models.DateTimeField('Start Year', default = None)
    End_Year = models.DateTimeField('End Year', default = None)
    GPA = models.FloatField(default = 0.0)
    Transcript_Link = models.URLField(max_length = 200, default = None)
    def __str__(self):
       return self.School_Name

class Work_Description(models.Model):
    Desc_Name = models.CharField(max_length = 200, default = None)
    Desc_Desc = models.CharField(max_length = 200, default = None)
    def __str__(self):
       return self.Desc_Name

class Work_Achievements(models.Model):
    Achievement_Name = models.CharField(max_length = 200, default = None)
    Achievement_Desc = models.CharField(max_length = 200, default = None)
    def __str__(self):
       return self.Achievement_Name

class Work_History(models.Model):
    Job_Title = models.CharField(max_length=200, default = None)
    Start_Year = models.DateTimeField('Start Year', default = None)
    End_Year = models.DateTimeField('End Year', default = None)
    Job_Desc = models.ManyToManyField(Work_Description)
    Work_Achiv = models.ManyToManyField(Work_Achievements)
    Present_Job = models.BooleanField(default = False)
    Phone_Number = models.IntegerField(default = None)
    def __str__(self):
       return self.Job_Title

class Skill(models.Model):
    Skill_Name = models.CharField(max_length = 200)
    Skill_Desc = models.CharField(max_length = 200)
    Years_Of_Exp = models.IntegerField(default = 0)
    Source_Type = models.ManyToManyField(Source_Type, default = None)
    Job_Key = models.ForeignKey(Work_History, on_delete=models.CASCADE, default = None, blank = True, null = True)
    Education_Key = models.ForeignKey(Education, on_delete=models.CASCADE, default = None, blank = True, null = True)
    def __str__(self):
       return self.Skill_Name

class Project(models.Model):
    Project_Name = models.CharField(max_length = 200, default = None)
    URL_Link = models.URLField(max_length = 200, default = None)
    Active = models.BooleanField(default = False)
    def __str__(self):
       return self.Project_Name

class Reference(models.Model):
    Reference_Name = models.CharField(max_length = 200, default = None)
    Reference_Number = models.IntegerField(default = None)
    Job_Key = models.ForeignKey(Work_History, on_delete=models.CASCADE, default = None)
    Education_Key = models.ForeignKey(Education, on_delete=models.CASCADE, default = None)
    Source_Type = models.ForeignKey(Source_Type, on_delete=models.CASCADE, default = None)
    def __str__(self):
       return self.Reference_Name

class ChatBot(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
       return self.question_text
