import sdRDM

from typing import Optional, Union
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

    genbank_protein_id: Optional[str] = Field(
        description="Systematic name of the protein.", default=None
    )

    amino_acid_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    function: Optional[str] = Field(description="Identifier of fubtion", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Rinkudatabase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="3f07fc7fb11976661ea4a442a53a32e40ed2e365"
    )
