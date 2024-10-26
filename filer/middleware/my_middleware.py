from django.http import HttpResponse
from django.core.signing import TimestampSigner
from django.shortcuts import redirect


def middleware(next):
    accept = ['/', '/api_reg/', '/api_auth/']
   
    def core_middleware(request):
        print(request.get_full_path())
        if not request.get_full_path() in accept:

            if request.session.get('token'):
                signer = TimestampSigner()
                try:
                    signer.unsign(request.session.get('token'), max_age=3600)
                except:
                    return redirect('authreg')
            if not request.session.get('token'):
                return redirect('authreg')

            print(request.session.get('token'))

        response = next(request)
        

        return response

    return core_middleware
