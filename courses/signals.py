from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Presence, PresenceHistory

@receiver(post_save, sender=Presence)
def create_presence_history(sender, instance, created, **kwargs):
    """
    Fungsi ini akan dijalankan setelah objek Presence disimpan.
    Ini akan membuat PresenceHistory dengan is_present=False jika
    waktu sekarang lebih besar dari waktu akhir (end_time) dan
    PresenceHistory dengan presence_id tertentu belum dibuat.
    """
    if created and instance.end_time and not PresenceHistory.objects.filter(presence=instance).exists():
        current_time = timezone.now().time()
        if current_time > instance.end_time:
            # Buat PresenceHistory baru dengan is_present=False
            PresenceHistory.objects.create(presence=instance, is_present=False)
