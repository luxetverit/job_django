from django.db import models

# Create your models here.
class BoardList(models.Model):
    pk_board = models.AutoField(primary_key=True)
    strBoardTitle = models.CharField(max_length=100)
    strBoardContents = models.TextField()
    nCnt = models.IntegerField()
    strName = models.CharField(max_length=50)
    putdatetime = models.CharField(max_length=24)

    class Meta:
        db_table = 'job_board'
        
    def __str__(self):
        return self.strBoardTitle


