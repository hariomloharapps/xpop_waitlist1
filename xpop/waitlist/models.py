from django.db import models
from django.utils import timezone


class WaitlistUser(models.Model):
    """
    Model to store waitlist users for XPOP
    """
    name = models.CharField(
        max_length=100,
        help_text="User's full name"
    )
    email = models.EmailField(
        unique=True,
        help_text="User's email address (must be unique)"
    )
    agree_to_help = models.BooleanField(
        default=False,
        help_text="Whether user agreed to help with beta testing"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text="When the user joined the waitlist"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last time the record was updated"
    )

    class Meta:
        ordering = ['-created_at']  # Latest first
        verbose_name = "Waitlist User"
        verbose_name_plural = "Waitlist Users"

    def __str__(self):
        beta_status = "Beta Tester" if self.agree_to_help else "Regular User"
        return f"{self.name} ({self.email}) - {beta_status}"

    @property
    def is_beta_tester(self):
        """Returns True if user agreed to help with beta testing"""
        return self.agree_to_help

    @property
    def joined_date(self):
        """Returns formatted date when user joined"""
        return self.created_at.strftime("%B %d, %Y")

    def save(self, *args, **kwargs):
        """Override save to ensure email is lowercase"""
        self.email = self.email.lower().strip()
        self.name = self.name.strip()
        super().save(*args, **kwargs)