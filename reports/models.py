from django.db import models

class Report(models.Model):
    campaign = models.ForeignKey('campaigns.Campaign', on_delete=models.CASCADE)
    sent_count = models.IntegerField(default=0)
    open_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    bounce_count = models.IntegerField(default=0)
    unsubscribe_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Relatório - {self.campaign.name}"
