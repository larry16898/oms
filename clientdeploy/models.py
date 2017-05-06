from django.db import models

# Create your models here.
class ClientSyncSetting(models.Model):
    PARENT_FOLDER = (
            ('autoPay','autoPay'),
            ('collect','collect'),
            ('cs_office','cs_office'),
            ('acc_office','acc_office'),
            ('it_office','it_office'),
            )
    name = models.CharField(max_length=50,verbose_name='软件名称')
    parent_folder = models.CharField(max_length=50,choices=PARENT_FOLDER,default='autoPay',verbose_name='父目录')
    sub_folder = models.CharField(max_length=50,verbose_name='子目录')
    version_num = models.CharField(max_length=5,verbose_name='版本号')
    host = models.CharField(max_length=20,verbose_name='同步源主机')
    username = models.CharField(max_length=50,verbose_name='同步账户')
    password = models.CharField(max_length=50,verbose_name='密码')
    ssh_host_key_fingerprint = models.CharField(max_length=100)
    shortcut_filename = models.CharField(max_length=50,verbose_name='桌面快捷方式')
    program_filename = models.CharField(max_length=50,verbose_name='可执行文件')
    file_mask = models.CharField(max_length=50,verbose_name='文件同步掩码',default='')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    class Meta:
        ordering = ('created',)



