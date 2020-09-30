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



