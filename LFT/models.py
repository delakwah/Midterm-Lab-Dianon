from django.db import models
from django.contrib.auth.models import User

# For user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

# For lost and found items
class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_lost = models.DateField()
    status = models.CharField(max_length=20, default="STATUS_CHOICES", choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    contact_info = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="items")

    def __str__(self):
        return self.item_name
    
# For message 
class Message(models.Model):
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE, related_name="messages")
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message for {self.item.item_name} by {self.sent_by.username}"
    
# For reports 
class Report(models.Model):
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE, related_name="reports")
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    message = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report for {self.item.item_name} by {self.reported_by.username}"
    
# To manage claims of found items
class Claim(models.Model):
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE, related_name="claims")
    claimed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="claims")
    message = models.TextField()
    date_claimed = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Claim for {self.item.item_name} by {self.claimed_by.username} ({'Approved' if self.is_approved else 'Pending'})"
