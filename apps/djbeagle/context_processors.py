from django.conf import settings

def context_processor(request):
    additions = {
        'DJBEAGLE_MEDIA_PREFIX' : settings.DJBEAGLE_MEDIA_PREFIX,
    }

    return additions    
