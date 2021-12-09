from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)  # staff name, i.e, John Smith
    email = models.EmailField(max_length=75)  # email fo the staff, i.e., johnsmith@uwm.edu
    username = models.CharField(max_length=100)  # user name of the staff for login, should be unique, i.e., john123
    password = models.CharField(max_length=25)  # password of the staff for login
    phoneNum = models.IntegerField()  # phone number of the staff, i.e., 4141234567 #TODO: max length 10?
    mailAddress = models.CharField(max_length=100)  # main address of staff i.e., 1234 N 12st

    # description: this function will look the Staff database and will return the user,
    #   if not exists, returns None
    # preconditions: username can not be None type
    # post conditions: user from the table if exists, will get returned
    # side effects: none
    def getUser(self, username):
        queryList = [Admin.objects.filter(username=username), Professor.objects.filter(username=username),
                     TA.objects.filter(username=username)]
        # a = queryList[0]
        print(queryList)
        user = None
        for query in queryList:
            if len(query) == 0:
                continue
            else:
                user = query[0]
        return user

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def getContactInfo(self, staff):
        q = None
        staffType = ['admin', 'prof', 'ta']
        if type(staff) is None:
            return None

        if staff not in staffType:
            return q
        else:
            if staff == 'admin':
                q = Admin.objects.all();
            elif staff == 'prof':
                q = Professor.objects.all()
            elif staff == 'ta':
                q = TA.objects.all()
            return q


    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Admin(Staff, models.Model):
    # description: this function will create a admin in Admin database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the admin will get created in Admin table
    # side effects: Admin table will get modified
    def createAdmin(self, fullName, email, username, password, phNumber, mailAdrs):
        # checking fields for validity/blanks
        if type(phNumber) != int:
            return None
        elif phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
        admin = Admin(name=fullName, email=email, username=username, password=password,
                      phoneNum=phNumber, mailAddress=mailAdrs)
        admin.save()
        print(admin)
        return admin

    # description: this function will create a professor in Professor database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the professor will get created in Professor table
    # side effects: Professor table will get modified
    def createProf(self, fullName, email, username, password, phNumber, mailAdrs):
        # checking fields for validity/blanks
        if type(phNumber) != int:
            return None
        elif phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
        prof = Professor(name=fullName, email=email, username=username, password=password,
                         phoneNum=phNumber, mailAddress=mailAdrs)
        prof.save()
        print(prof)
        return prof

    # description: this function will create a ta in TA database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the ta will get created in TA table
    # side effects: TA table will get modified
    def createTA(self, fullName, email, username, password, phNumber, mailAdrs):
        # checking fields for validity/blanks
        if type(phNumber) != int:
            return None
        elif phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
        ta = TA(name=fullName, email=email, username=username, password=password,
                phoneNum=phNumber, mailAddress=mailAdrs)
        ta.save()
        print(ta)
        return ta

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def createCourse(self, nm, sec, cre, pre, des):
        if nm == "" or nm[0] == "":
            return None
        if sec == "" or sec[0] == "":
            return None
        if cre == "" or cre[0] == "":
            return None
        if not (cre.isdecimal()):
            return None
        else:
            co = Course(name=nm, section=sec, credits=cre, prereqs=pre, description=des)
            co.save()
            return co

#<<<<<<< Baljinder-Singh
    # description: this function will allow the creation of new Lab
    # preconditions: name should be similar to course that the lab will assign to
    # post conditions: the new lab for course will get created
    # side effects: Lab table will have this new lab in it
    def createLab(self, name, section):
        lab = None
        if not name or not section:
            return lab

        # cheery pick bad case before creating a lab
        if type(name) is int:
            return lab
        elif name == "":
            return lab
        elif name[0] == " ":
            return lab
        elif type(name[0]) is int:
            return lab
        elif name[0] in [' @_!#$%^&*()<>?/\|}{~: ']:
            return lab
        elif type(section) is not int:
            return lab
        elif type(section) is float:
            return lab
        elif section > 99999:
            return lab
        elif section < 1:
            return lab

        courseExist = Course.objects.filter(name=name)
        courseSimToLab = Course.objects.filter(name=name, section=section)
        labExist = Lab.objects.filter(name=name, section=section)
        if not courseExist:
            return lab
        elif courseSimToLab:
            return lab
        elif labExist:
            return lab

        lab = Lab(name=name, section=section)
        lab.save()

        return lab

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def assignStaff(self):
        pass
#=======
    def assignProf(self, prof, course):
        pass

    def assignTA(self, TA, course):
#>>>>>>> master
        pass


class Professor(Staff, models.Model):

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def assignTA(self, ta, lab):
        pass

    # inputs: none
    # functionality: makes sure caller is a professor then queries database for assignments
    # outputs: returns all assignments related to professor in database
    def viewCourseAssignments(self, course):
        queryList = [Assignment.objects.filter(owner=self.username, course=course)]
        print(queryList)
        if len(queryList) == 0:
            return None
        return queryList

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def createAssignment(self, name, dueDate, course):
        assignment = Assignment(owner=self, name=name, dueDate=dueDate, course=course)
        assignment.save()
        return assignment




class TA(Staff, models.Model):

    def viewAssignments(self):
        pass

    #class: coursetoAssignment
    # class: LabToAssignment

class Assignment(models.Model):
    name = models.CharField(max_length=100)  # name of the assignment, i.e... Homework 5
    owner = models.CharField(max_length=100)  # username of the instructor who created the assignment, i.e... jrock22
    dueDate = models.CharField(max_length=100)
    course = models.CharField(max_length=100)  # name of the course this assignment is tied to

    def __str__(self):
        return self.owner+"-"+self.name+"-"+self.dueDate

class Course(models.Model):
    name = models.CharField(max_length=100)  # name of the course, i.e., SC361
    section = models.IntegerField()  # section of this course i.e., 401
    credits = models.IntegerField()  # number of credits for this course i.e., 3
    prereqs = models.CharField(max_length=100)  # prereqs that this course required
    description = models.CharField(max_length=255)  # quick summary of the course

    # description: this function will look the Course database and will return the course,
    #   if not exists, returns None
    # preconditions: courseName and sectionNumber can not be None
    # post conditions: returns specified course
    # side effects: none
    def getCourse(self, courseName, sectionNumber):
        queryList = [Course.objects.filter(name=courseName).filter(section=sectionNumber)]
        print(queryList)
        course = None
        for query in queryList:
            if len(query) == 0:
                continue
            else:
                course = query[0]
        return course

    def __str__(self):
        return self.name + "-"+self.section


class Lab(models.Model):
    # name of the lab, should be similar to course name
    # since its is assigning to a course, i.e.,  CS361
    name = models.CharField(max_length=100)
    section = models.IntegerField()  # section of lab, i.e., 802

    def __str__(self):
        return self.name + "-" + str(self.section)


class LabToCourse(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "Lab " + self.ta.__str__() + " is assigned to course " + self.course.__str__()


class ProfessorToCourse(models.Model):
    # This table is cascaded, mean if any of those field get deleted the whole will get deleted from this table
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "Professor " + self.professor.__str__() + " is assigned to course " + self.course.__str__()


class TAToCourse(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "TA " + self.ta.__str__() + " is assigned to course " + self.course.__str__()


class TAToLab(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return "TA " + self.ta.__str__() + " is assigned to lab " + self.lab.__str__()
