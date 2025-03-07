from plugs.manager import PlugManager
from plugs.plug import Plug

scribe_plug = Plug(
    name="care_scribe",
    package_name="git+https://github.com/ohcnetwork/care_scribe.git",
    version="@master",
    configs={},
)

hcx_plugin = Plug(
    name="hcx",
    package_name="git+https://github.com/ohcnetwork/care_hcx.git",
    version="@hcx_emr",
    configs={},
)
abdm_plug = Plug(
    name="abdm",
    package_name="git+https://github.com/ohcnetwork/care_abdm.git",
    version="@abdm_emr",
    configs={},
)


plugs = [hcx_plugin, scribe_plug,abdm_plug]
manager = PlugManager(plugs)
