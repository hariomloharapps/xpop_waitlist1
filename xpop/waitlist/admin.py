from django.contrib import admin
from .models import WaitlistUser


@admin.register(WaitlistUser)
class WaitlistUserAdmin(admin.ModelAdmin):
    """
    Admin interface for WaitlistUser model
    """
    list_display = [
        'name', 'email', 'agree_to_help', 'created_at', 'is_beta_tester'
    ]
    list_filter = [
        'agree_to_help', 'created_at'
    ]
    search_fields = [
        'name', 'email'
    ]
    readonly_fields = [
        'created_at', 'updated_at', 'is_beta_tester'
    ]
    ordering = ['-created_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('name', 'email')
        }),
        ('Preferences', {
            'fields': ('agree_to_help',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def is_beta_tester(self, obj):
        """Display beta tester status"""
        return "✅ Yes" if obj.is_beta_tester else "❌ No"
    is_beta_tester.short_description = "Beta Tester"
    
    def get_queryset(self, request):
        """Optimize database queries"""
        return super().get_queryset(request).select_related()

    # Custom admin actions
    actions = ['mark_as_beta_testers', 'mark_as_regular_users']

    def mark_as_beta_testers(self, request, queryset):
        """Mark selected users as beta testers"""
        updated = queryset.update(agree_to_help=True)
        self.message_user(request, f'{updated} users marked as beta testers.')
    mark_as_beta_testers.short_description = "Mark selected users as beta testers"

    def mark_as_regular_users(self, request, queryset):
        """Mark selected users as regular users"""
        updated = queryset.update(agree_to_help=False)
        self.message_user(request, f'{updated} users marked as regular users.')
    mark_as_regular_users.short_description = "Mark selected users as regular users"