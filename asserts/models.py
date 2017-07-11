from django.db import models

# Create your models here.
class AssertCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别名称')
    comment = models.TextField(verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return self.name

class Assert(models.Model):
    ASSERTS_STATUS = (
            ('in using','使用中'),
            ('idle','闲置'),
            ('broken','损坏待修')

            )
    #name = models.CharField(max_length=50,verbose_name='资产名称')
    assert_code = models.CharField(max_length=50,verbose_name='资产编码',default='NULL')
    category = models.ForeignKey(AssertCategory, verbose_name='资产类别',related_name='assert_set', null=True)
    assert_status = models.CharField(max_length=20,choices=ASSERTS_STATUS,default='idle',verbose_name='状态')
    location = models.CharField(max_length=100,verbose_name='位置',null=True,blank=True)
    owner = models.CharField(max_length=50,verbose_name='使用人',null=True,blank=True)
    ip_address = models.CharField(max_length=100,verbose_name='IP地址',null=True,blank=True)
    comment = models.TextField(verbose_name='备注',null=True, blank=True)

    def __str__(self):
        return self.assert_code

class AssertChangeRelation(models.Model):
    assert_related = models.ForeignKey(Assert, verbose_name='关联的资产', related_name='change_record_set')
    change_record_related = models.ForeignKey('AssertChangeRecord', verbose_name='变更记录', related_name='assert_set')
    created = models.DateTimeField(auto_now_add=True, verbose_name='变更创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='变更修改时间')

class AssertChangeRecord(models.Model):
    name = models.CharField(max_length=50,verbose_name='资产变更')
    change_content = models.TextField(verbose_name='变更内容')
    related_assert = models.ManyToManyField(Assert, through=AssertChangeRelation, related_name='change_records')
