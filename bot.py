


print("""
██╗░░██╗░█████╗░███╗░░░███╗███████╗  
██║░░██║██╔══██╗████╗░████║██╔════╝  
███████║██║░░██║██╔████╔██║█████╗░░  
██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░  
██║░░██║╚█████╔╝██║░╚═╝░██║███████╗  
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝  

██╗░░░██╗░██████╗███████╗██████╗░  ██████╗░░█████╗░████████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░░██║╚█████╗░█████╗░░██████╔╝  ██████╦╝██║░░██║░░░██║░░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗  ██╔══██╗██║░░██║░░░██║░░░
╚██████╔╝██████╔╝███████╗██║░░██║  ██████╦╝╚█████╔╝░░░██║░░░
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░

R.I.P
Логи:""")


 
  
         
  
# Covid

    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get('http://wttr.in/{citys}_2&lang=rus.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command("weather", prefixes=".") & filters.me)
async def weather(client: Client, message: Message):
    city = message.command[1]
    await message.edit("```Processing the request...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=en")
    await message.edit(f"```City: {r.text}```")

