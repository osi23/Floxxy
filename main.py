from tkinter import *
import math,random
from tkinter import messagebox
import os
import smtplib
import random
import time
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen

#Function

def reset():
    textReceipt.delete(1.0, END)
    e_caroWhite.set('0')
    e_whitesecrete.set('0')
    e_carotune.set('0')
    e_pawpaw.set('0')
    e_precious.set('0')
    e_DermaX.set('0')
    e_SkinM.set('0')
    e_DodoSG.set('0')
    e_Nevia.set('0')
    e_NatureM.set('0')

    e_carowhitesoap.set('0')
    e_clinicclearsoap.set('0')
    e_glutawhitesoap.set('0')
    e_whitesecretsoap.set('0')
    e_tura.set('0')
    e_kojic.set('0')
    e_carotunesoap.set('0')
    e_ashanti.set('0')
    e_totmosol.set('0')
    e_kbrother.set('0')

    e_damatol.set('0')
    e_sofine.set('0')
    e_soulmate.set('0')
    e_dodoskingoldBSC.set('0')
    e_pawpawBSC.set('0')
    e_whitesecretBSC.set('0')
    e_jraBSC.set('0')
    e_nanoxtraBSC.set('0')
    e_carotuneBSC.set('0')
    e_stayyoungBSC.set('0')

    e_smart.set('0')
    e_explore.set('0')
    e_storm.set('0')
    e_dubai.set('0')
    e_club.set('0')
    e_happi.set('0')
    e_maliza.set('0')
    e_rigs.set('0')
    e_rising.set('0')
    e_balila.set('0')

    #DISABLED the EntryField
    textcaroWhite.config(state=DISABLED)
    textwhitesecrete.config(state=DISABLED)
    textcarotune.config(state=DISABLED)
    textpawpaw.config(state=DISABLED)
    textprecious.config(state=DISABLED)
    textDermaX.config(state=DISABLED)
    textSkinM.config(state=DISABLED)
    textDodoSG.config(state=DISABLED)
    textNevia.config(state=DISABLED)
    textNatureM.config(state=DISABLED)

    textcarowhitesoap.config(state=DISABLED)
    textclinicclearsoap.config(state=DISABLED)
    textglutawhitesoap.config(state=DISABLED)
    textwhitesecretsoap.config(state=DISABLED)
    texttura.config(state=DISABLED)
    textkojic.config(state=DISABLED)
    textcarotunesoap.config(state=DISABLED)
    textashanti.config(state=DISABLED)
    texttotmosol.config(state=DISABLED)
    textkbrother.config(state=DISABLED)

    textdamatol.config(state=DISABLED)
    textsofine.config(state=DISABLED)
    textsoulmate.config(state=DISABLED)
    textdodoskingoldBSC.config(state=DISABLED)
    textpawpawBSC.config(state=DISABLED)
    textwhitesecretBSC.config(state=DISABLED)
    textjraBSC.config(state=DISABLED)
    textnanoxtraBSC.config(state=DISABLED)
    textcarotuneBSC.config(state=DISABLED)
    textstayyoungBSC.config(state=DISABLED)

    textsmart.config(state=DISABLED)
    textexplore.config(state=DISABLED)
    textstorm.config(state=DISABLED)
    textdubai.config(state=DISABLED)
    textclub.config(state=DISABLED)
    texthappi.config(state=DISABLED)
    textmaliza.config(state=DISABLED)
    textrigs.config(state=DISABLED)
    textrising.config(state=DISABLED)
    textbalila.config(state=DISABLED)

#VARIABLE To uncheck the check button
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)

    # Variable To set Cost to Disable

    CostOfBodyCreamVar.set('')
    costofsoapvar.set('')
    costofhaircreamvar.set('')
    costofperfumevar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:

        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            #auth=copy the authorization key link
            url='https://www.fast2sms.com/dev/bulk'

           # params={
             #   'authorization':auth,
               # 'message':message,
               # 'numbers':number,
             #   'sender=id':'FSTSMS',
               # 'route':'p',
              #  'language':'english'
            #}

        root2=Toplevel()

        root2.title("SEND BILL")
        root2.config(bg='white')
        root2.geometry('485x620+50+50')

        logoImage=PhotoImage(file='env.png')
        label=Label(root2,image=logoImage,bg='white')
        label.pack()

        numberLabel=Label(root2,text='Mobel Number',font=('arial',18,'bold underline'),bg='white',fg='#8B8000')
        numberLabel.pack()

        numberfield=Entry(root2,font=('arial',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel=Label(root2,text='Bill Details',font=('arial',18,'underline'),bg='white',fg='#8B8000')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=10)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')


        if CostOfBodyCreamVar.get()!='0 Naira':
            textarea.insert(END,f' Cost Of Body Cream\t\t\t{priceOfBodyCream}Naira\n')

        if costofsoapvar.get() != '0 Naira':
            textarea.insert(END, f' Cost Soap\t\t\t{priceofSoap}Naira\n')

        if costofhaircreamvar.get() != '0 Naira':
            textarea.insert(END, f' Cost Of Hair Cream\t\t\t{priceofhaircream}Naira\n')

        if costofperfumevar.get() != '0 Naira':
            textarea.insert(END, f' Cost Of Perfume\t\t\t{priceofperfume}Naira\n')

        textarea.insert(END, f' Sub Total\t\t\t{subtotalofItems}Naira\n')
        textarea.insert(END, f' Service Tax\t\t\t{50}Naira\n\n')
        textarea.insert(END, f' Total Cost \t\t\t{subtotalofItems+50}Naira\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='#8B8000',bd=7,relief=GROOVE,
                          command=send_msg)
        sendButton.pack()

        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Successfully Saved')


def Receipt():
    global billnumber,date
    if CostOfBodyCreamVar.get()!='' or costofsoapvar.get()!='' or costofhaircreamvar.get()!=''or costofperfumevar.get()!='':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\tCost Of Items(Naira)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_caroWhite.get()!='0':
            textReceipt.insert(END,f'Caro White\t\t\t{int(e_caroWhite.get())*2000}\n\n')

        if e_whitesecrete.get()!='0':
            textReceipt.insert(END,f'White Secret\t\t\t{int(e_whitesecrete.get())*1400}\n\n')

        if e_carotune.get()!='0':
            textReceipt.insert(END,f'Carotune\t\t\t{int(e_carotune.get())*1000}\n\n')

        if e_pawpaw.get()!='0':
            textReceipt.insert(END,f'Pawpaw\t\t\t{int(e_pawpaw.get())*1200}\n\n')

        if e_precious.get()!='0':
            textReceipt.insert(END,f'Precious\t\t\t{int(e_precious.get())*1400}\n\n')

        if e_DermaX.get()!='0':
            textReceipt.insert(END,f'Derma Xtra\t\t\t{int(e_DermaX.get())*1300}\n\n')

        if e_SkinM.get()!='0':
            textReceipt.insert(END,f'Skin Magnet\t\t\t{int(e_SkinM.get())*1400}\n\n')

        if e_DodoSG.get()!='0':
            textReceipt.insert(END,f'Dodo Skin Gold\t\t\t{int(e_DodoSG.get())*10000}\n\n')

        if e_Nevia.get()!='0':
            textReceipt.insert(END,f'Nevia\t\t\t{int(e_Nevia.get())*2000}\n\n')

        if e_NatureM.get()!='0':
            textReceipt.insert(END,f'Nature Magic\t\t\t{int(e_NatureM.get())*1700}\n\n')


        if e_carowhitesoap.get()!='0':
            textReceipt.insert(END,f'Caro White Soap\t\t\t{int(e_carowhitesoap.get())*2000}\n\n')

        if e_clinicclearsoap.get()!='0':
            textReceipt.insert(END,f'Clinic Clear\t\t\t{int(e_clinicclearsoap.get())*1400}\n\n')

        if e_glutawhitesoap.get()!='0':
            textReceipt.insert(END,f'Gluta White Soap\t\t\t{int(e_glutawhitesoap.get())*1000}\n\n')

        if e_whitesecretsoap.get()!='0':
            textReceipt.insert(END,f'White Secret Soap\t\t\t{int(e_whitesecretsoap.get())*1200}\n\n')

        if e_tura.get()!='0':
            textReceipt.insert(END,f'Tura\t\t\t{int(e_tura.get())*1400}\n\n')

        if e_kojic.get()!='0':
            textReceipt.insert(END,f'Kojic\t\t\t{int(e_kojic.get())*1300}\n\n')

        if e_carotunesoap.get()!='0':
            textReceipt.insert(END,f'Carotune Soap\t\t\t{int(e_carotunesoap.get())*1400}\n\n')

        if e_ashanti.get()!='0':
            textReceipt.insert(END,f'Ashanti\t\t\t{int(e_ashanti.get())*10000}\n\n')

        if e_totmosol.get()!='0':
            textReceipt.insert(END,f'Totmosol\t\t\t{int(e_totmosol.get())*2000}\n\n')

        if e_kbrother.get()!='0':
            textReceipt.insert(END,f'K Brother\t\t\t{int(e_kbrother.get())*1700}\n\n')


        if e_damatol.get()!='0':
            textReceipt.insert(END,f'Damatol\t\t\t{int(e_damatol.get())*1000}\n\n')

        if e_sofine.get()!='0':
            textReceipt.insert(END,f'So Fine\t\t\t{int(e_sofine.get())*1400}\n\n')

        if e_soulmate.get()!='0':
            textReceipt.insert(END,f'Soul Mate\t\t\t{int(e_soulmate.get())*1000}\n\n')

        if e_dodoskingoldBSC.get()!='0':
            textReceipt.insert(END,f'Dodo Skin Gold\t\t\t{int(e_dodoskingoldBSC.get())*1200}\n\n')

        if e_pawpawBSC.get()!='0':
            textReceipt.insert(END,f'Pawpaw\t\t\t{int(e_pawpawBSC.get())*1400}\n\n')

        if e_whitesecretBSC.get()!='0':
            textReceipt.insert(END,f'White Secret BSc\t\t\t{int(e_whitesecretBSC.get())*1300}\n\n')

        if e_carotuneBSC.get()!='0':
            textReceipt.insert(END,f'Carotune\t\t\t{int(e_carotune.get())*1400}\n\n')

        if e_jraBSC.get()!='0':
            textReceipt.insert(END,f'JRA BSC\t\t\t{int(e_jraBSC.get())*10000}\n\n')

        if e_stayyoungBSC.get()!='0':
            textReceipt.insert(END,f'Stay Young\t\t\t{int(e_stayyoungBSC.get())*2000}\n\n')

        if e_nanoxtraBSC.get()!='0':
            textReceipt.insert(END,f'Nano Xtra BSC\t\t\t{int(e_nanoxtraBSC.get())*1700}\n\n')



        if e_smart.get()!='0':
            textReceipt.insert(END,f'Smart\t\t\t{int(e_smart.get())*2000}\n\n')

        if e_explore.get()!='0':
            textReceipt.insert(END,f'Explore\t\t\t{int(e_explore.get())*1400}\n\n')

        if e_storm.get()!='0':
            textReceipt.insert(END,f'Storm\t\t\t{int(e_storm.get())*1000}\n\n')

        if e_dubai.get()!='0':
            textReceipt.insert(END,f'Dubai\t\t\t{int(e_dubai.get())*1200}\n\n')

        if e_club.get()!='0':
            textReceipt.insert(END,f'Cotton Club\t\t\t{int(e_club.get())*1400}\n\n')

        if e_happi.get()!='0':
            textReceipt.insert(END,f'Happiness\t\t\t{int(e_happi.get())*1300}\n\n')

        if e_maliza.get()!='0':
            textReceipt.insert(END,f'Maliza\t\t\t{int(e_maliza.get())*1400}\n\n')

        if e_rigs.get()!='0':
            textReceipt.insert(END,f'Rigs\t\t\t{int(e_rigs.get())*10000}\n\n')

        if e_rising.get()!='0':
            textReceipt.insert(END,f'Rising\t\t\t{int(e_rising.get())*2000}\n\n')

        if e_balila.get()!='0':
            textReceipt.insert(END,f'Balila\t\t\t{int(e_balila.get())*1700}\n\n')



        textReceipt.insert(END, '***************************************************************\n')

        if CostOfBodyCreamVar.get()!='0 Naira':
            textReceipt.insert(END,f' Cost Of Body Cream\t\t\t{priceOfBodyCream}Naira\n\n')

        if costofsoapvar.get() != '0 Naira':
            textReceipt.insert(END, f' Cost Soap\t\t\t{priceofSoap}Naira\n\n')

        if costofhaircreamvar.get() != '0 Naira':
            textReceipt.insert(END, f' Cost Of Hair Cream\t\t\t{priceofhaircream}Naira\n\n')

        if costofperfumevar.get() != '0 Naira':
            textReceipt.insert(END, f' Cost Of Perfume\t\t\t{priceofperfume}Naira\n\n')

        textReceipt.insert(END, f' Sub Total\t\t\t{subtotalofItems}Naira\n\n')
        textReceipt.insert(END, f' Service Tax\t\t\t{50}Naira\n\n')
        textReceipt.insert(END, f' Total Cost \t\t\t{subtotalofItems+50}Naira\n\n')
        textReceipt.insert(END, '***************************************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is Selected')


#Price Of Items
def totalcost():
    global priceOfBodyCream,priceofSoap,priceofhaircream,priceofperfume,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
        var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0 or \
        var31.get() != 0 or var32.get() != 0 or var33.get() != 0 or var34.get() != 0 or var35.get() != 0 or \
        var36.get() != 0 or var37.get() != 0 or var38.get() != 0 or var39.get() != 0 or var40.get() != 0:
        item1 = int(e_caroWhite.get())
        item2 = int(e_whitesecrete.get())
        item3 = int(e_carotune.get())
        item4 = int(e_pawpaw.get())
        item5 = int(e_precious.get())
        item6 = int(e_DermaX.get())
        item7 = int(e_SkinM.get())
        item8 = int(e_DodoSG.get())
        item9 = int(e_Nevia.get())
        item10 = int(e_NatureM.get())

        item11 = int(e_carowhitesoap.get())
        item12 = int(e_clinicclearsoap.get())
        item13 = int(e_glutawhitesoap.get())
        item14 = int(e_whitesecretsoap.get())
        item15 = int(e_tura.get())
        item16 = int(e_kojic.get())
        item17 = int(e_carotunesoap.get())
        item18 = int(e_ashanti.get())
        item19 = int(e_totmosol.get())
        item20 = int(e_kbrother.get())

        item21 = int(e_damatol.get())
        item22 = int(e_sofine.get())
        item23 = int(e_soulmate.get())
        item24 = int(e_dodoskingoldBSC.get())
        item25 = int(e_pawpawBSC.get())
        item26 = int(e_whitesecretBSC.get())
        item27 = int(e_carotuneBSC.get())
        item28 = int(e_jraBSC.get())
        item29 = int(e_stayyoungBSC.get())
        item30 = int(e_nanoxtraBSC.get())

        item31 = int(e_smart.get())
        item32 = int(e_explore.get())
        item33 = int(e_storm.get())
        item34 = int(e_dubai.get())
        item35 = int(e_club.get())
        item36 = int(e_happi.get())
        item37 = int(e_maliza.get())
        item38 = int(e_rigs.get())
        item39 = int(e_rising.get())
        item40 = int(e_balila.get())

        priceOfBodyCream = (item1 * 2000) + (item2 * 1400) + (item3 * 1000) + (item4 * 1200) + (item5 * 1400) + (
                    item6 * 1300) \
                           + (item7 * 1400) + (item8 * 1000) + (item9 * 2000) + (item10 * 1700)

        priceofSoap = (item11 * 2000) + (item12 * 1400) + (item13 * 1000) + (item14 * 1200) + (item15 * 1400) + (
                    item16 * 1300) \
                      + (item17 * 1400) + (item18 * 1000) + (item19 * 2000) + (item20 * 1700)

        priceofhaircream = (item21 * 1000) + (item22 * 1400) + (item23 * 1000) + (item24 * 1200) + (item25 * 1400) + (
                    item26 * 1300) \
                           + (item27 * 1400) + (item28 * 1000) + (item29 * 2000) + (item30 * 1700)

        priceofperfume = (item31 * 2000) + (item32 * 1400) + (item33 * 1000) + (item34 * 1200) + (item35 * 1400) + (
                    item36 * 1300) \
                         + (item37 * 1400) + (item38 * 1000) + (item39 * 2000) + (item40 * 1700)

        CostOfBodyCreamVar.set(str(priceOfBodyCream)+'Naira')
        costofsoapvar.set(str(priceofSoap)+'Naira')
        costofhaircreamvar.set(str(priceofhaircream)+'Naira')
        costofperfumevar.set(str(priceofperfume)+'Naira')

        subtotalofItems=priceOfBodyCream+priceofSoap+priceofhaircream+priceofperfume
        subtotalvar.set(str(subtotalofItems)+'Naira')

        servicetaxvar.set('50 Naira')

        totalcost=subtotalofItems+50
        totalcostvar.set(str(totalcost)+'Naira')

    else:
        messagebox.showerror('Error','No Item Is Selected')

def caroWhite():
    if var1.get()==1:
        textcaroWhite.config(state=NORMAL)
        textcaroWhite.delete(0,END)
        textcaroWhite.focus()
    else:
        textcaroWhite.config(state=DISABLED)
        e_caroWhite.set('0')

def whitesecrete():
    if var2.get()==1:
        textwhitesecrete.config(state=NORMAL)
        textwhitesecrete.delete(0,END)
        textwhitesecrete.focus()
    else:
        textwhitesecrete.config(state=DISABLED)
        e_whitesecrete.set('0')

def carotune():
    if var3.get()==1:
        textcarotune.config(state=NORMAL)
        textcarotune.delete(0,END)
        textcarotune.focus()
    else:
        textcarotune.config(state=DISABLED)
        e_carotune.set('0')

def pawpaw():
    if var4.get()==1:
        textpawpaw.config(state=NORMAL)
        textpawpaw.delete(0,END)
        textpawpaw.focus()
    else:
        textpawpaw.config(state=DISABLED)
        e_pawpaw.set('0')

def precious():
    if var5.get()==1:
        textprecious.config(state=NORMAL)
        textprecious.delete(0,END)
        textprecious.focus()
    else:
        textprecious.config(state=DISABLED)
        e_precious.set('0')

def DermaX():
    if var6.get()==1:
        textDermaX.config(state=NORMAL)
        textDermaX.delete(0,END)
        textDermaX.focus()
    else:
        textDermaX.config(state=DISABLED)
        e_DermaX.set('0')

def SkinM():
    if var7.get()==1:
        textSkinM.config(state=NORMAL)
        textSkinM.delete(0,END)
        textSkinM.focus()
    else:
        textSkinM.config(state=DISABLED)
        e_SkinM.set('0')

def DodoSG():
    if var8.get()==1:
        textDodoSG.config(state=NORMAL)
        textDodoSG.delete(0,END)
        textDodoSG.focus()
    else:
        textDodoSG.config(state=DISABLED)
        e_DodoSG.set('0')

def Nevia():
    if var9.get()==1:
        textNevia.config(state=NORMAL)
        textNevia.delete(0,END)
        textNevia.focus()
    else:
        textNevia.config(state=DISABLED)
        e_Nevia.set('0')

def NatureM():
    if var10.get()==1:
        textNatureM.config(state=NORMAL)
        textNatureM.delete(0,END)
        textNatureM.focus()
    else:
        textNatureM.config(state=DISABLED)
        e_NatureM.set('0')



def carowhitesoap():
    if var11.get()==1:
        textcarowhitesoap.config(state=NORMAL)
        textcarowhitesoap.delete(0,END)
        textcarowhitesoap.focus()
    else:
        textcarowhitesoap.config(state=DISABLED)
        e_carowhitesoap.set('0')

def clinicclearsoap():
    if var12.get()==1:
        textclinicclearsoap.config(state=NORMAL)
        textclinicclearsoap.delete(0,END)
        textclinicclearsoap.focus()
    else:
        textclinicclearsoap.config(state=DISABLED)
        e_clinicclearsoap.set('0')

def glutawhitesoap():
    if var13.get()==1:
        textglutawhitesoap.config(state=NORMAL)
        textglutawhitesoap.delete(0,END)
        textglutawhitesoap.focus()
    else:
        textglutawhitesoap.config(state=DISABLED)
        e_glutawhitesoap.set('0')

def whitesecretsoap():
    if var14.get()==1:
        textwhitesecretsoap.config(state=NORMAL)
        textwhitesecretsoap.delete(0,END)
        textwhitesecretsoap.focus()
    else:
        textwhitesecretsoap.config(state=DISABLED)
        e_whitesecretsoap.set('0')

def Tura():
    if var15.get()==1:
        texttura.config(state=NORMAL)
        texttura.delete(0,END)
        texttura.focus()
    else:
        texttura.config(state=DISABLED)
        e_tura.set('0')

def kojic():
    if var16.get()==1:
        textkojic.config(state=NORMAL)
        textkojic.delete(0,END)
        textkojic.focus()
    else:
        textkojic.config(state=DISABLED)
        e_kojic.set('0')

def carotunesoap():
    if var17.get()==1:
        textcarotunesoap.config(state=NORMAL)
        textcarotunesoap.delete(0,END)
        textcarotunesoap.focus()
    else:
        textcarotunesoap.config(state=DISABLED)
        e_carotunesoap.set('0')

def ashanti():
    if var18.get()==1:
        textashanti.config(state=NORMAL)
        textashanti.delete(0,END)
        textashanti.focus()
    else:
        textashanti.config(state=DISABLED)
        e_ashanti.set('0')

def totmosol():
    if var19.get()==1:
        texttotmosol.config(state=NORMAL)
        texttotmosol.delete(0,END)
        texttotmosol.focus()
    else:
        texttotmosol.config(state=DISABLED)
        e_totmosol.set('0')

def KBrother():
    if var20.get()==1:
        textkbrother.config(state=NORMAL)
        textkbrother.delete(0,END)
        textkbrother.focus()
    else:
        textkbrother.config(state=DISABLED)
        e_kbrother.set('0')

def damatol():
    if var21.get()==1:
        textdamatol.config(state=NORMAL)
        textdamatol.delete(0,END)
        textdamatol.focus()
    else:
        textdamatol.config(state=DISABLED)
        e_damatol.set('0')

def sofine():
    if var22.get()==1:
        textsofine.config(state=NORMAL)
        textsofine.delete(0,END)
        textsofine.focus()
    else:
        textsofine.config(state=DISABLED)
        e_sofine.set('0')

def soulmate():
    if var23.get()==1:
        textsoulmate.config(state=NORMAL)
        textsoulmate.delete(0,END)
        textsoulmate.focus()
    else:
        textsoulmate.config(state=DISABLED)
        e_soulmate.set('0')

def dodoskingoldBSC():
    if var24.get()==1:
        textdodoskingoldBSC.config(state=NORMAL)
        textdodoskingoldBSC.delete(0,END)
        textdodoskingoldBSC.focus()
    else:
        textdodoskingoldBSC.config(state=DISABLED)
        e_dodoskingoldBSC.set('0')

def pawpawBSC():
    if var25.get()==1:
        textpawpawBSC.config(state=NORMAL)
        textpawpawBSC.delete(0,END)
        textpawpawBSC.focus()
    else:
        textpawpawBSC.config(state=DISABLED)
        e_pawpawBSC.set('0')

def whitesecretBSC():
    if var26.get()==1:
        textwhitesecretBSC.config(state=NORMAL)
        textwhitesecretBSC.delete(0,END)
        textwhitesecretBSC.focus()
    else:
        textwhitesecretBSC.config(state=DISABLED)
        e_whitesecretBSC.set('0')

def carotuneBSC():
    if var27.get()==1:
        textcarotuneBSC.config(state=NORMAL)
        textcarotuneBSC.delete(0,END)
        textcarotuneBSC.focus()
    else:
        textcarotuneBSC.config(state=DISABLED)
        e_carotuneBSC.set('0')

def jraBSC():
    if var28.get()==1:
        textjraBSC.config(state=NORMAL)
        textjraBSC.delete(0,END)
        textjraBSC.focus()
    else:
        textjraBSC.config(state=DISABLED)
        e_jraBSC.set('0')

def stayyoungBSC():
    if var29.get()==1:
        textstayyoungBSC.config(state=NORMAL)
        textstayyoungBSC.delete(0,END)
        textstayyoungBSC.focus()
    else:
        textstayyoungBSC.config(state=DISABLED)
        e_stayyoungBSC.set('0')

def nanoxtraBSC():
    if var30.get()==1:
        textnanoxtraBSC.config(state=NORMAL)
        textnanoxtraBSC.delete(0,END)
        textnanoxtraBSC.focus()
    else:
        textnanoxtraBSC.config(state=DISABLED)
        e_nanoxtraBSC.set('0')


def smart():
    if var31.get() == 1:
        textsmart.config(state=NORMAL)
        textsmart.delete(0, END)
        textsmart.focus()
    else:
        textsmart.config(state=DISABLED)
        e_smart.set('0')

def explore():
    if var32.get() == 1:
        textexplore.config(state=NORMAL)
        textexplore.delete(0, END)
        textexplore.focus()
    else:
        textexplore.config(state=DISABLED)
        e_explore.set('0')

def storm():
    if var33.get() == 1:
        textstorm.config(state=NORMAL)
        textstorm.delete(0, END)
        textstorm.focus()
    else:
        textstorm.config(state=DISABLED)
        e_storm.set('0')

def dubai():
    if var34.get() == 1:
        textdubai.config(state=NORMAL)
        textdubai.delete(0, END)
        textdubai.focus()
    else:
        textdubai.config(state=DISABLED)
        e_dubai.set('0')

def club():
    if var35.get() == 1:
        textclub.config(state=NORMAL)
        textclub.delete(0, END)
        textclub.focus()
    else:
        textclub.config(state=DISABLED)
        e_club.set('0')

def happi():
    if var36.get() == 1:
        texthappi.config(state=NORMAL)
        texthappi.delete(0, END)
        texthappi.focus()
    else:
        texthappi.config(state=DISABLED)
        e_happi.set('0')

def maliza():
    if var37.get() == 1:
        textmaliza.config(state=NORMAL)
        textmaliza.delete(0, END)
        textmaliza.focus()
    else:
        textmaliza.config(state=DISABLED)
        e_maliza.set('0')

def rigs():
    if var38.get() == 1:
        textrigs.config(state=NORMAL)
        textrigs.delete(0, END)
        textrigs.focus()
    else:
        textrigs.config(state=DISABLED)
        e_rigs.set('0')

def rising():
    if var39.get() == 1:
        textrising.config(state=NORMAL)
        textrising.delete(0, END)
        textrising.focus()
    else:
        textrising.config(state=DISABLED)
        e_rising.set('0')

def balila():
    if var40.get() == 1:
        textbalila.config(state=NORMAL)
        textbalila.delete(0, END)
        textbalila.focus()
    else:
        textbalila.config(state=DISABLED)
        e_balila.set('0')



root=Tk()


root.geometry("1920x1080+-10+0")
root.title("Floxxy Costmetic Store By Osikhena")
root.config(width=1500,height=600, bg="#8B8000")
topFrame=Frame(root,bd=10,relief=RIDGE,bg='#8B8000')
topFrame.pack(side=TOP)
Labeltitle=Label(topFrame,text='Floxxy Cosmetic Store',font=('arial',30,'bold'),fg='red4',bd=9,bg='#8B8000',width=51)
Labeltitle.grid(row=0,column=0)


#FRAME
menuFrame=Frame(root,bd=0,relief=RIDGE,bg="#8B8000")
menuFrame.pack(side=LEFT)

costFrame=LabelFrame(menuFrame,bd=2,relief=SUNKEN,text= "Cost",font=('arial',12,'bold'),fg='gold',bg='#8B8000',pady=1)
costFrame.pack(side=BOTTOM)

customerFrame=LabelFrame(root,bd=10,relief=GROOVE,
                         text="Customer Details",font=("arial",15,'bold'),fg='gold',bg='#8B8000')
customerFrame.place(x=0,y=70,width=1270)

BodyCreamFrame=LabelFrame(menuFrame,text='Body Cream',font=('arial',19,'bold'),bd=5,relief=GROOVE,bg="#8B8000",fg='red4')
BodyCreamFrame.pack(side=LEFT)

SoapFrame=LabelFrame(menuFrame,text='Soap',font=('arial',19,'bold'),bd=5,relief=GROOVE,bg="#8B8000",fg='red4')
SoapFrame.pack(side=LEFT)

HairFrame=LabelFrame(menuFrame,text='Hair',font=('arial',19,'bold'),bd=5,relief=GROOVE,bg="#8B8000",fg='red4')
HairFrame.pack(side=LEFT)

PerfumeFrame=LabelFrame(menuFrame,text='Perfume',font=('arial',19,'bold'),bd=5,relief=GROOVE,bg="#8B8000",fg='red4')
PerfumeFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=10,relief=GROOVE,bg='#8B8000')
rightFrame.pack(side=RIGHT)

CalculatorFrame=Frame(rightFrame,bd=0,relief=GROOVE,bg="#8B8000")
CalculatorFrame.pack()

ReceiptFrame=Frame(rightFrame,bd=4,relief=GROOVE,bg="#8B8000")
ReceiptFrame.pack()

ButtonFrame=Frame(rightFrame,bd=3,relief=GROOVE,bg="#8B8000")
ButtonFrame.pack()

# VARIABLES

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()
var37 = IntVar()
var38 = IntVar()
var39 = IntVar()
var40 = IntVar()

#Entry Field For Body Cream Variable
e_caroWhite=StringVar()
e_whitesecrete=StringVar()
e_carotune=StringVar()
e_pawpaw=StringVar()
e_precious=StringVar()
e_DermaX=StringVar()
e_SkinM=StringVar()
e_DodoSG=StringVar()
e_Nevia=StringVar()
e_NatureM=StringVar()


#Entry Field For Soap Variable
e_carowhitesoap=StringVar()
e_clinicclearsoap=StringVar()
e_glutawhitesoap=StringVar()
e_whitesecretsoap=StringVar()
e_tura=StringVar()
e_kojic=StringVar()
e_carotunesoap=StringVar()
e_ashanti=StringVar()
e_totmosol=StringVar()
e_kbrother=StringVar()

#Entry Field For Hair Variable
e_damatol=StringVar()
e_sofine=StringVar()
e_soulmate=StringVar()
e_dodoskingoldBSC=StringVar()
e_pawpawBSC=StringVar()
e_whitesecretBSC=StringVar()
e_jraBSC=StringVar()
e_nanoxtraBSC=StringVar()
e_carotuneBSC=StringVar()
e_stayyoungBSC=StringVar()


#Entry Field For Perfume Variable
e_smart=StringVar()
e_explore=StringVar()
e_storm=StringVar()
e_dubai=StringVar()
e_club=StringVar()
e_happi=StringVar()
e_maliza=StringVar()
e_rigs=StringVar()
e_rising=StringVar()
e_balila=StringVar()

#Cost Variable
CostOfBodyCreamVar=StringVar()
costofsoapvar=StringVar()
costofhaircreamvar=StringVar()
costofperfumevar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_caroWhite.set('0')
e_whitesecrete.set('0')
e_carotune.set('0')
e_pawpaw.set('0')
e_precious.set('0')
e_DermaX.set('0')
e_SkinM.set('0')
e_DodoSG.set('0')
e_Nevia.set('0')
e_NatureM.set('0')

e_carowhitesoap.set('0')
e_clinicclearsoap.set('0')
e_glutawhitesoap.set('0')
e_whitesecretsoap.set('0')
e_tura.set('0')
e_kojic.set('0')
e_carotunesoap.set('0')
e_ashanti.set('0')
e_totmosol.set('0')
e_kbrother.set('0')


e_damatol.set('0')
e_sofine.set('0')
e_soulmate.set('0')
e_dodoskingoldBSC.set('0')
e_pawpawBSC.set('0')
e_whitesecretBSC.set('0')
e_jraBSC.set('0')
e_nanoxtraBSC.set('0')
e_carotuneBSC.set('0')
e_stayyoungBSC.set('0')

e_smart.set('0')
e_explore.set('0')
e_storm.set('0')
e_dubai.set('0')
e_club.set('0')
e_happi.set('0')
e_maliza.set('0')
e_rigs.set('0')
e_rising.set('0')
e_balila.set('0')



#Body Cream

caroWhite= Checkbutton(BodyCreamFrame, text='Caro W', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var1,command=caroWhite)
caroWhite.grid(row=0, column=0, sticky='w')

whitesecrete = Checkbutton(BodyCreamFrame, text='White S', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var2,command=whitesecrete)
whitesecrete.grid(row=1, column=0, sticky='w')

carotune = Checkbutton(BodyCreamFrame, text='Caro t', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var3,command=carotune)
carotune.grid(row=2, column=0, sticky='w')

pawpaw = Checkbutton(BodyCreamFrame, text='Pawpaw', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var4,command=pawpaw)
pawpaw.grid(row=3, column=0, sticky='w')

precious = Checkbutton(BodyCreamFrame, text='Precious', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var5,command=precious)
precious.grid(row=4, column=0, sticky='w')

DermaX= Checkbutton(BodyCreamFrame, text='Derma X', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var6,command=DermaX)
DermaX.grid(row=5, column=0, sticky='w')

SkinM = Checkbutton(BodyCreamFrame, text='Skin M', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var7,command=SkinM)
SkinM.grid(row=6, column=0, sticky='w')

DodoSG= Checkbutton(BodyCreamFrame, text='Dodo S G', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var8,command=DodoSG)
DodoSG.grid(row=7, column=0, sticky='w')

Nevia = Checkbutton(BodyCreamFrame, text='Nevia', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var9,command=Nevia)
Nevia.grid(row=8, column=0, sticky='w')

NatureM = Checkbutton(BodyCreamFrame, text='Nature M', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var10,command=NatureM)
NatureM.grid(row=9, column=0, sticky='w')



#Soap

Carowhitesoap= Checkbutton(SoapFrame, text='Caro W', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var11,command=carowhitesoap)
Carowhitesoap.grid(row=0, column=0, sticky='w')

clinicclearsoap = Checkbutton(SoapFrame, text='Clinic C', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var12,command=clinicclearsoap)
clinicclearsoap.grid(row=1, column=0, sticky='w')

glutawhitesoap = Checkbutton(SoapFrame, text='Gluta W', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var13,command=glutawhitesoap)
glutawhitesoap.grid(row=2, column=0, sticky='w')

whitesecretsoap = Checkbutton(SoapFrame, text='White S', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var14,command=whitesecretsoap)
whitesecretsoap.grid(row=3, column=0, sticky='w')

Tura = Checkbutton(SoapFrame, text='Tura', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var15,command=Tura)
Tura.grid(row=4, column=0, sticky='w')

Kojic = Checkbutton(SoapFrame, text='Kojic', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var16,command=kojic)
Kojic.grid(row=5, column=0, sticky='w')

carotunesoap = Checkbutton(SoapFrame, text='Carotune', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var17,command=carotunesoap)
carotunesoap.grid(row=6, column=0, sticky='w')

ashanti = Checkbutton(SoapFrame, text='Ashanti', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var18,command=ashanti)
ashanti.grid(row=7, column=0, sticky='w')

totmosol = Checkbutton(SoapFrame, text='Totmosol', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var19,command=totmosol)
totmosol.grid(row=8, column=0, sticky='w')

KBrother = Checkbutton(SoapFrame, text='K.Brother', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var20,command=KBrother)
KBrother.grid(row=9, column=0, sticky='w')




#Hair, Face and Tubes

damatol= Checkbutton(HairFrame, text='Damatol' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var21,command=damatol)
damatol.grid(row=0, column=0, sticky='w')

sofine = Checkbutton(HairFrame, text='So Fine', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var22,command=sofine)
sofine.grid(row=1, column=0, sticky='w')

soulmate= Checkbutton(HairFrame, text='Soul Mate' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var23,command=soulmate)
soulmate.grid(row=2, column=0, sticky='w')

dodoskingoldBSC= Checkbutton(HairFrame, text='DodoBSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var24,command=dodoskingoldBSC)
dodoskingoldBSC.grid(row=3, column=0, sticky='w')

pawpawBSC= Checkbutton(HairFrame, text='PawBSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var25,command=pawpawBSC)
pawpawBSC.grid(row=4, column=0, sticky='w')

whitesecretBSC= Checkbutton(HairFrame, text='WhiteBSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var26,command=whitesecretBSC)
whitesecretBSC.grid(row=5, column=0, sticky='w')

carotuneBSC= Checkbutton(HairFrame, text='Carot BSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var27,command=carotuneBSC)
carotuneBSC.grid(row=6, column=0, sticky='w')

jraBSC= Checkbutton(HairFrame, text='JRA BSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var28,command=jraBSC)
jraBSC.grid(row=7, column=0, sticky='w')

stayyoungBSC= Checkbutton(HairFrame, text='Stay Y BSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var29,command=stayyoungBSC)
stayyoungBSC.grid(row=8, column=0, sticky='w')

nanoxtraBSC= Checkbutton(HairFrame, text='Nano X BSC' , font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var30,command=nanoxtraBSC)
nanoxtraBSC.grid(row=9, column=0, sticky='w')



#Perfumes

smart = Checkbutton(PerfumeFrame, text='Smart', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var31,command=smart)
smart.grid(row=0, column=0, sticky='w')

explore = Checkbutton(PerfumeFrame, text='Explore', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var32,command=explore)
explore.grid(row=1, column=0, sticky='w')

storm = Checkbutton(PerfumeFrame, text='Storm', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var33,command=storm)
storm.grid(row=2, column=0, sticky='w')

dubai = Checkbutton(PerfumeFrame, text='Dubai', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var34,command=dubai)
dubai.grid(row=3, column=0, sticky='w')

club = Checkbutton(PerfumeFrame, text='Club', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var35,command=club)
club.grid(row=4, column=0, sticky='w')

happi = Checkbutton(PerfumeFrame, text='Happi', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var36,command=happi)
happi.grid(row=5, column=0, sticky='w')

maliza = Checkbutton(PerfumeFrame, text='Maliza', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var37,command=maliza)
maliza.grid(row=6, column=0, sticky='w')

rigs = Checkbutton(PerfumeFrame, text='Rigs', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var38,command=rigs)
rigs.grid(row=7, column=0, sticky='w')

rising= Checkbutton(PerfumeFrame, text='Rising', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var39,command=rising)
rising.grid(row=8, column=0, sticky='w')

balila = Checkbutton(PerfumeFrame, text='Balila', font=('arial', 14, 'bold'),bg="#8B8000",
                        onvalue=1, offvalue=0, variable=var40,command=balila)
balila.grid(row=9, column=0, sticky='w')


#Entry Fields for Body Cream
textcaroWhite=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_caroWhite)
textcaroWhite.grid(row=0,column=1)

textwhitesecrete=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_whitesecrete)
textwhitesecrete.grid(row=1,column=1)

textcarotune=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_carotune)
textcarotune.grid(row=2,column=1)

textpawpaw=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_pawpaw)
textpawpaw.grid(row=3,column=1)

textprecious=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_precious)
textprecious.grid(row=4,column=1)

textDermaX=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_DermaX)
textDermaX.grid(row=5,column=1)

textSkinM=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_SkinM)
textSkinM.grid(row=6,column=1)

textDodoSG=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_DodoSG)
textDodoSG.grid(row=7,column=1)


textNevia=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_Nevia)
textNevia.grid(row=8,column=1)

textNatureM=Entry(BodyCreamFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_NatureM)
textNatureM.grid(row=9,column=1)




#Entry Fields for Soap
textcarowhitesoap=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_carowhitesoap)
textcarowhitesoap.grid(row=0,column=1)

textclinicclearsoap=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_clinicclearsoap)
textclinicclearsoap.grid(row=1,column=1)

textglutawhitesoap=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_glutawhitesoap)
textglutawhitesoap.grid(row=2,column=1)

textwhitesecretsoap=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_whitesecretsoap)
textwhitesecretsoap.grid(row=3,column=1)

texttura=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_tura)
texttura.grid(row=4,column=1)

textkojic=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_kojic)
textkojic.grid(row=5,column=1)

textcarotunesoap=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_carotunesoap)
textcarotunesoap.grid(row=6,column=1)

textashanti=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_ashanti)
textashanti.grid(row=7,column=1)

texttotmosol=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_totmosol)
texttotmosol.grid(row=8,column=1)

textkbrother=Entry(SoapFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_kbrother)
textkbrother.grid(row=9,column=1)



#Hair, Face and Tubes
textdamatol=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_damatol)
textdamatol.grid(row=0,column=1)

textsofine=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_sofine)
textsofine.grid(row=1,column=1)

textsoulmate=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_soulmate)
textsoulmate.grid(row=2,column=1)

textdodoskingoldBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_dodoskingoldBSC)
textdodoskingoldBSC.grid(row=3,column=1)

textpawpawBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_pawpawBSC)
textpawpawBSC.grid(row=4,column=1)

textwhitesecretBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_whitesecretBSC)
textwhitesecretBSC.grid(row=5,column=1)

textcarotuneBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_carotuneBSC)
textcarotuneBSC.grid(row=6,column=1)

textjraBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_jraBSC)
textjraBSC.grid(row=7,column=1)

textstayyoungBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_stayyoungBSC)
textstayyoungBSC.grid(row=8,column=1)

textnanoxtraBSC=Entry(HairFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_nanoxtraBSC)
textnanoxtraBSC.grid(row=9,column=1)


#Entry Fields for Perfume
textsmart=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_smart)
textsmart.grid(row=0,column=1)

textexplore=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_explore)
textexplore.grid(row=1,column=1)

textstorm=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_storm)
textstorm.grid(row=2,column=1)

textdubai=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_dubai)
textdubai.grid(row=3,column=1)

textclub=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_club)
textclub.grid(row=4,column=1)

texthappi=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_happi)
texthappi.grid(row=5,column=1)

textmaliza=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_maliza)
textmaliza.grid(row=6,column=1)

textrigs=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_rigs)
textrigs.grid(row=7,column=1)

textrising=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_rising)
textrising.grid(row=8,column=1)

textbalila=Entry(PerfumeFrame, font=('arial', 14, 'bold'),bd=7,width=6,
                    state=DISABLED,textvariable=e_balila)
textbalila.grid(row=9,column=1)


#Cost Labels & Entry Fields
labelCostOfBodyCream=Label(costFrame,text='Cost Of Body Cream',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelCostOfBodyCream.grid(row=0,column=0)

textCostOfBodyCream=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=CostOfBodyCreamVar)
textCostOfBodyCream.grid(row=0,column=1,padx=41)

labelCostOfSoap=Label(costFrame,text='Cost Of Soap',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelCostOfSoap.grid(row=1,column=0)

textCostOfSoap=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=costofsoapvar)
textCostOfSoap.grid(row=1,column=1,padx=41)

labelCostOfHairCream=Label(costFrame,text='Cost Of Hair Cream',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelCostOfHairCream.grid(row=2,column=0)

textCostOfHairCream=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=costofhaircreamvar)
textCostOfHairCream.grid(row=2,column=1,padx=41)

labelCostOfPerfume=Label(costFrame,text='Cost Of Perfume',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelCostOfPerfume.grid(row=3,column=0)

textCostOfPerfume=Entry(costFrame,font=('arial', 14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=costofperfumevar)
textCostOfPerfume.grid(row=3,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',14,'bold'),bg="#8B8000",fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=14,
                          state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons
buttonTotal=Button(ButtonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg="#8B8000",bd=3,padx=5,
                  command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(ButtonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg="#8B8000",bd=3,padx=5,
                     command=Receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(ButtonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg="#8B8000",bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(ButtonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg="#8B8000",bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(ButtonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg="#8B8000",bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#Text Area For Receipt
textReceipt=Text(ReceiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''


calculatorField=Entry(CalculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,columnspan=4)

button7=Button(CalculatorFrame,text='7',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(CalculatorFrame,text='8',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(CalculatorFrame,text='9',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(CalculatorFrame,text='+',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(CalculatorFrame,text='4',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(CalculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(CalculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(CalculatorFrame,text='-',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(CalculatorFrame,text='1',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(CalculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(CalculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=lambda : buttonClick('3'))
button3.grid(row=3,column=2)

buttonMultiplication=Button(CalculatorFrame,text='*',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6, width=6
               ,command=lambda : buttonClick('*'))
buttonMultiplication.grid(row=3,column=3)

buttonanswer=Button(CalculatorFrame,text='Ans',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=answer)
buttonanswer.grid(row=4,column=0)

buttonclear=Button(CalculatorFrame,text='Clear',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6
               ,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(CalculatorFrame,text='0',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6,
               command=lambda : buttonClick('0'))
button0.grid(row=4,column=2)

buttonDivision=Button(CalculatorFrame,text='/',font=('arial',16,'bold'),fg='red4',bg='yellow',bd=6,width=6,
               command=lambda : buttonClick('/'))
buttonDivision.grid(row=4,column=3)




#CUSTOMER DETAILS
#customer entryfield
e_CustomerName=StringVar()
e_PhoneNo=StringVar()
e_Email=StringVar()

#Customer Name
labelCustomerName=Label(customerFrame,text="Customer Name",font=('arial',16,'bold'),bg='#8B8000',fg='red4')
labelCustomerName.grid(row=0,column=0)

textCustomerName=Entry(customerFrame,font=('arial',16,'bold' ),bd=6,width=14,textvariable=e_CustomerName)
textCustomerName.grid(row=0,column=1,padx=40)


#Customer Phone No.
labelPhoneNo=Label(customerFrame,text="Phone No.",font=('arial',16,'bold'),bg='#8B8000',fg='red4')
labelPhoneNo.grid(row=0,column=2)

textPhoneNo=Entry(customerFrame,font=('arial',16,'bold' ),bd=6,width=14,textvariable=e_PhoneNo)
textPhoneNo.grid(row=0,column=3, padx=40)

#Email
labelEmail=Label(customerFrame,text="Email",font=('arial',16,'bold'),bg='#8B8000',fg='red4')
labelEmail.grid(row=0,column=4)

textEmail=Entry(customerFrame,font=('arial',16,'bold' ),bd=6,width=14,textvariable=e_Email)
textEmail.grid(row=0,column=5, padx=40)




root.mainloop()