import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Systematic name of the protein.")

    amino_acid_sequence: str = Field(
        ..., description="The amino acid sequence of the protein sequence object."
    )

    nr_id: Optional[str] = Field(
        description="Identifier for the NCBI NR database", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Rinkudatabase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="39e585f2114ac7a13cac72b4b7e30f914110f300"
    )