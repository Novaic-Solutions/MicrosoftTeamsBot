#import config
#import session
#import asyncio
#from web.webServer import DevopsBotWebServer


#ngrok http 3978 --domain=gladly-electric-mudfish.ngrok-free.app --host-header rewrite

#config._prepare_config()
#session._prepare_sessions()


# async def main():
#     #NOTE: Here two processes would be started up. One for the web server, 
#     #   a second for the Adapter. Between the two would be a queue.
#     webServer = DevopsBotWebServer()
#     await webServer.start()
    

# #NOTE: Looking into overriding the ADAPTER class to use the DevopsAdapter instead of the BotFrameworkAdapter
# #       Also looking to see how the Bot class is used with the process_activity method

# if __name__ == "__main__":
#     asyncio.run(main())

from multiprocessing import JoinableQueue
import time

import config
from procs.botProcs import BotProcess, WebServerProcess

config._prepare_config()

def main():
    resultQueue = JoinableQueue()
    webServerProc = WebServerProcess(resultQueue)
    botProc = BotProcess(resultQueue)

    webServerProc.start()
    botProc.start()

    while True:
        try:

            if not webServerProc.is_alive():
                print("Web Server Process is dead")
                webServerProc.terminate()
                webServerProc.join(1)
                webServerProc = WebServerProcess(resultQueue)
                webServerProc.start()
            w
            if not botProc.is_alive():
                print("Bot Process is dead")
                botProc.terminate()
                botProc.join(1)
                botProc = BotProcess(resultQueue)
                botProc.start()

            else:
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            webServerProc.terminate()
            botProc.terminate()
            webServerProc.join(1)
            botProc.join(1)
            resultQueue.close()
            webServerProc.close()
            botProc.close()
            break
            


if __name__ == "__main__":
    main()