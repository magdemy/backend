from django.contrib import admin

class CustomModelAdmin(admin.ModelAdmin):
    list_filter = ['deleted_at']
    exclude = ['deleted_at']

    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        return qs