from ovos_utils.log import LOG
from ovos_plugin_manager.stt import STT, StreamingSTT, StreamThread


class WitSTT(STT):
    """STT interface for the OVOS-HTTP-STT-Server"""
    def __init__(self, config=None):
        super().__init__(config)
        self.token = self.config.get("token")

    def execute(self, audio, language=None):
        LOG.warning("WitSTT language should be configured at wit.ai settings.")
        return self.recognizer.recognize_wit(audio, self.token)

WitSTTConfig = {}
