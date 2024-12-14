import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render
from .models import wallet

def createWallet(request):
    username=''
    currentBalance='0'
    FormerBalance='0'
    ModifiedBy=''
    DateModified=''
    
  
    
    if request.method == 'POST': 
        username= request.POST['username']
        currentBalance= request.POST['currentBalance']
        formerBalance= request.POST['formerBalance']
        modifiedBy= request.POST['modifiedBy']
        try:
            Wallet = wallet()
            Wallet.Username= username
            Wallet.CurrentBalance=currentBalance
            Wallet.FormerBalance=formerBalance
            Wallet.ModifiedBy= modifiedBy
            Wallet.DateModified= datetime.datetime.now()

            Wallet.save()
        except ():
            print('A database Error occurred')

    
    return render(request,'createWallet.html' )

def viewWallets(request):

    Wallets = wallet.objects.all()
   
        
    return render(request, 'viewWallet.html', {'WalletList': Wallets } )


# Create your views here.
