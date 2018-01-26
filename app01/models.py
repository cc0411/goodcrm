#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#3个字节一个汉字
class Customer(models.Model):
    '''客户表'''
    name = models.CharField(max_length=32,blank=True,null=True)
    qq = models.CharField(max_length=24,unique=True)
    phone = models.CharField(max_length=32,blank=True,null=True)
    source_choices = ((1,'QQ'),(2,'转介绍'),(3,'官网'),(4,'百度'),(5,'51CTO'))
    source = models.SmallIntegerField(choices=source_choices )
    referral_from = models.CharField(max_length=32,blank=True,null=True)
    consult_course = models.ForeignKey("Course",verbose_name=u"咨询课程")
    content = models.TextField(verbose_name=u'咨询详情')
    consultant = models.ForeignKey("UserProfile")
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField("Tag",blank=True,null=True)
    def __unicode__(self):
        return self.qq
    class Meta:
        verbose_name = u'客户表'
        verbose_name_plural = u'客户表'
class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=32,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u'标签'
        verbose_name = u'标签'
class CustomerFollowUp(models.Model):
    '''客户跟进'''
    customer = models.ForeignKey("Customer")
    content = models.TextField(u"跟进内容")
    consultant = models.ForeignKey("UserProfile")
    date = models.DateField(auto_now_add=True)
    intention_choices =((0,'2周内报名'),(1,'一个月内报名'),(2,'近期无计划'),(3,'已报其他机构'),(4,'已报名'))
    intention = models.SmallIntegerField(choices=intention_choices)
    def __unicode__(self):
        return "%s-%s" %(self.customer.qq,self.intention)
    class Meta:
        verbose_name = u'客户跟进'
        verbose_name_plural = u'客户跟进'
class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=64,unique=True)
    price = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField(verbose_name=u'周期')
    outline = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'课程表'
        verbose_name_plural = u'课程表'
class Branch(models.Model):
    '''校区'''
    name = models.CharField(max_length=32,unique=True)
    addr = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'校区'
        verbose_name_plural = u'校区'
class ClassList(models.Model):
    ''''班级表'''
    branch = models.ForeignKey("Branch")
    course = models.ForeignKey("Course")
    semester = models.PositiveSmallIntegerField(verbose_name=u'学期')
    teachers = models.ManyToManyField("UserProfile")
    class_type_choices = ((0,'面授脱产'),(1,'面授周末'),(2,'网络'))
    class_type = models.SmallIntegerField(choices=class_type_choices,verbose_name=u'班级类型')
    start_date= models.DateField(verbose_name=u'开班日期')
    def __unicode__(self):
        return "%s-%s-%s" %(self.branch,self.course,self.semester)
    class Meta:
        unique_together =('branch','course','semester')
        verbose_name_plural = u'班级表'
        verbose_name = u'班级表'
class CourseRecord(models.Model):
    '''上课记录'''
    from_class = models.ForeignKey("ClassList",verbose_name=u'班级')
    day_num = models.PositiveSmallIntegerField(verbose_name=u'第几节课')
    teacher = models.ForeignKey("UserProfile")
    outline = models.TextField(verbose_name=u'本节课大纲')
    date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return "%s-%s" %(self.from_class,self.day_num)
    class Meta:
        unique_together = ('from_class','day_num')
        verbose_name = u'上课记录'
        verbose_name_plural = u'上课记录'
class StudyRecord(models.Model):
    '''学习记录'''
    student = models.ForeignKey("Enrollment")
    course_record = models.ForeignKey("CourseRecord")
    attendance_choices = ((0,'已签到'),(1,'迟到'),(2,'缺勤'),(3,'早退'))
    attendance = models.SmallIntegerField(choices=attendance_choices,default=0)
    score_choices = ((100,'A+'),(90,'A'),(85,"B+"),(80,"B"),(70,'C'),(60,'C-'))
    score = models.SmallIntegerField(choices=score_choices)
    memo = models.TextField(blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return "%s-%s-%s"  %(self.student,self.course_record,self.score)
    class Meta:
        unique_together = ('student','course_record')
        verbose_name = u'学习记录'
        verbose_name_plural=u'学习记录'
class Enrollment(models.Model):
    '''报名表'''
    customer = models.ForeignKey("Customer")
    enroller_class = models.ForeignKey("ClassList",verbose_name=u'所报班级')
    consultant = models.ForeignKey("UserProfile",verbose_name=u'课程顾问')
    contract_agreed = models.BooleanField(default=False,verbose_name=u'学员已同意')
    contract_approved = models.BooleanField(default=False,verbose_name=u'合同已审核')
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s-%s"  %(self.customer,self.enroller_class)
    class Meta:
        unique_together = ('customer','enroller_class')
        verbose_name = u'报名表'
        verbose_name_plural = u'报名表'
class Payment(models.Model):
    '''缴费记录'''
    customer = models.ForeignKey("Customer")
    amount = models.PositiveSmallIntegerField(default=500,verbose_name=u'金额')
    consultant = models.ForeignKey("UserProfile")
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey("Course",verbose_name="所报课程")
    def __unicode__(self):
        return  "%s-%s" %(self.customer,self.amount)
    class Meta:
        verbose_name_plural = u'缴费记录'
        verbose_name = u'缴费记录'
class UserProfile(models.Model):
    '''帐号表'''
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    roles = models.ManyToManyField("Role",blank=True,null=True)
    def __unicode__(self):
        return self.name
    class  Meta:
        verbose_name_plural =u'帐号表'
        verbose_name_plural = u'帐号表'
class Role(models.Model):
    '''角色表'''
    name = models.CharField(max_length=32)
    menus = models.ManyToManyField('Menu',blank=True,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u'角色表'
        verbose_name = u'角色表'
class Menu(models.Model):
    '''菜单'''
    name = models.CharField(max_length=32)
    url_name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u'菜单'
        verbose_name = u'菜单'


















