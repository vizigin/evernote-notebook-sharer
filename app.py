import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient, NoteStore, UserStore

dev_token = "auth_token_sender"
# dev_token2 = "auth_token_receiver"

class EvernoteSession:
    
    def __init__(self, dev_token):
        self.token = dev_token
        self.client = EvernoteClient(token=dev_token)
        self.userStore = self.client.get_user_store()
        self.noteStore = self.client.get_note_store()
        
    def shareNotebook(self, notebookGuid, email=None):
        sharedNotebook = Types.SharedNotebook()
        sharedNotebook.requireLogin = True
        sharedNotebook.notebookGuid = notebookGuid
        sharedNotebook.email = email
        sharedNotebook.privilege = Types.SharedNotebookPrivilegeLevel.READ_NOTEBOOK_PLUS_ACTIVITY

        user = self.userStore.getUser()
        shardId = user.shardId
        newSharedNotebook = c.noteStore.shareNotebook(sharedNotebook, "Test message")

        # linkedNotebook = Types.LinkedNotebook()
    	# linkedNotebook.sharedNotebookGlobalId = newSharedNotebook.globalId
    	# linkedNotebook.shareName = notebookName
        # linkedNotebook.username = "d_vizigin"
    	# linkedNotebook.shardId = shardId
    	# newLinkedNotebook = c.noteStore.createLinkedNotebook(dev_token2, linkedNotebook)
        
        # old way: url = "%s/shard/%s/share/%s/" % (EN_URL, shardId, newSharedNotebook.shareKey)
        url = ""
        return url
        
if __name__=="__main__":
    c = EvernoteSession(dev_token)
    
    print "Connected as '%s'" % (c.userStore.getUser().username)

    while 1:        
        print
        notebooks = c.noteStore.listNotebooks()
        sharedNotebooks = c.noteStore.listSharedNotebooks()

        ctr = 0
        for notebook in notebooks:
            print "Notebook [%d] '%s'" % (ctr, notebook.name)
            ctr += 1
            
            for sharedNotebook in sharedNotebooks:
                if sharedNotebook.notebookGuid == notebook.guid:
                    print "- Shared with %s" % (sharedNotebook.email)
        
        print
        ch = raw_input("Share notebook number: ")
        print
        
        if not len(ch):
            break
        
        n = int(ch)        
        notebook = notebooks[n]

        email = "d.vizigin@livetyping.com"
        url = c.shareNotebook(notebook.guid, email)
        print "Send URL to %s => %s" % (email, url)