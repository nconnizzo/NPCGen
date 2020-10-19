from dataclasses import dataclasses
@dataclass
# defining the NPC class
# this class contains an IDnumber, a name, sex, then an array of attributes, and a set of traits        
class NPC:
    npc_id: int
    name: str
    sex: str
    attribs
    traits

#defining the attributes class
#this class contains essentially a subclass -- attribs will be nested within an NPC
#remains to be seen whether to create a separate class for these is worthwhile
class attribs
    alt: int
    app: int
    con: int
    cri: int
    edu: int
    hea: int
    pro: int
    rel: int
    smt: int
    soc: int
    wea: int

#defining the traits class
#the idea here is that every trait will have 4 attributes. tr-keystat is the primary attribute on which the trait is based (e.g. selecting the traitgroup)
#tr-statmin and tr-statmax set the upper and lower bound of how to create the list of available traits. (however that will be done)
#tr-name is lastly the name of the trait which is what will be appended to the subclass of the NPC

class trait
    tr-name: str
    tr-keystat: str
    tr-statmin: int
    tr-statmax: int

#defining the relationship class
#relationships are objects that connect two NPCs and describe the nature of their relationship
#rel-ID is the unique ID for the relationship
#rel-cat is the "category" of relationship it is
#members should be a (python) array that can have people appended to it. since we are using an array, we can use ordination (e.g. 0 for first member, 1 for 2nd member, etc.) to show hierarchy

class relationship
    rel-ID: int
    rel-cat: str
    members
    
#defining the structure class
#structures consist of basic information about the structure itself and links to all the roles contained within.




#defining the role class
#roles are separate from structures but are linked within (should we go this way). this allows NPCgen to be able to reuse roles across multiple structures
#roles have a name and potentially any number of tags (a simple list since order is not important)

class role
    rolename: str
    tags