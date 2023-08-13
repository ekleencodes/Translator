from tkinter import*
import googletrans
import textblob
from tkinter import ttk,messagebox

root=Tk()
root.title("Translator")
root.geometry("880x300")

def translate_it():
    text2.delete(1.0,END)
    try:
        for key,value in languages.items():
            if(value==text1_combo.get()):
               from_language_key=key
        for key,value in languages.items():
            if(value==text2_combo.get()):
               to_language_key=key 
               
        words=textblob.TextBlob(text1.get(1.0,END))
        translated_text=words.translate(from_lang=from_language_key,to=to_language_key)
        
        text2.insert(1.0,translated_text)
        
        
    except Exception as e:
        messagebox.showerror("Translator",e)
        

def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    
languages=googletrans.LANGUAGES
language_list=list(languages.values())

    

text1=Text(root,height=10,width=40)
text1.grid(row=0,column=0,pady=20,padx=10)

text1_btn=Button(root,text="Translate!",font=("Helvetica",24),command=translate_it)
text1_btn.grid(row=0,column=1,padx=10)

text2=Text(root,height=10,width=40)
text2.grid(row=0,column=2,pady=20,padx=10)

text1_combo=ttk.Combobox(root,width=50,value=language_list)
text1_combo.current(21) 
text1_combo.grid(row=1,column=0)

text2_combo=ttk.Combobox(root,width=50,value=language_list)
text2_combo.current(26) 
text2_combo.grid(row=2,column=2)

btn=Button(root,text="Clear",command=clear)
btn.grid(row=2,column=1)

root.mainloop()