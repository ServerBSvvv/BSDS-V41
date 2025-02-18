from Classes.Packets.PiranhaMessage import PiranhaMessage


import Configuration

from Classes.Packets.PiranhaMessage import PiranhaMessage


class LoginOkMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 1

    def encode(self, fields, player):
        self.writeLong(player.ID[0], player.ID[1])
        self.writeLong(player.ID[0], player.ID[1])
        self.writeString(player.Token)
        self.writeString()
        self.writeString()
        self.writeInt(41)
        self.writeInt(148)
        self.writeInt(1)
        self.writeString("dev")
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString("CA")
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeInt(2)
        self.writeString('https://game-assets.brawlstarsgame.com')
        self.writeString('http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com')
        self.writeInt(2)
        self.writeString('https://event-assets.brawlstars.com')
        self.writeString('https://24b999e6da07674e22b0-8209975788a0f2469e68e84405ae4fcf.ssl.cf2.rackcdn.com/event-assets')
        self.writeVint(0)
        self.writeCompressedString(b'')
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString('https://play.google.com/store/apps/details?id=com.supercell.brawlstars')
        self.writeString()
        self.writeBoolean(True)

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["HomeID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["FacebookID"] = self.readString()
        fields["GamecenterID"] = self.readString()
        fields["ServerMajorVersion"] = self.readInt()
        fields["ContentVersion"] = self.readInt()
        fields["ServerBuild"] = self.readInt()
        fields["ServerEnvironment"] = self.readString()
        fields["SessionCount"] = self.readInt()
        fields["PlayTimeSeconds"] = self.readInt()
        fields["DaysSinceStartedPlaying"] = self.readInt()
        fields["FacebookAppID"] = self.readString()
        fields["ServerTime"] = self.readString()
        fields["AccountCreatedDate"] = self.readString()
        fields["StartupCooldownSeconds"] = self.readInt()
        fields["GoogleServiceID"] = self.readString()
        fields["LoginCountry"] = self.readString()
        fields["KunlunID"] = self.readString()
        fields["Tier"] = self.readInt()
        fields["TencentID"] = self.readString()

        ContentUrlCount = self.readInt()
        fields["GameAssetsUrls"] = []
        for i in range(ContentUrlCount):
            fields["GameAssetsUrls"].append(self.readString())

        EventUrlCount = self.readInt()
        fields["EventAssetsUrls"] = []
        for i in range(EventUrlCount):
            fields["EventAssetsUrls"].append(self.readString())

        fields["SecondsUntilAccountDeletion"] = self.readVint()
        fields["SupercellIDToken"] = self.readCompressedString()
        fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        fields["isSupercellIDEligible"] = self.readBoolean()
        fields["LineID"] = self.readString()
        fields["SessionID"] = self.readString()
        fields["KakaoID"] = self.readString()
        fields["UpdateURL"] = self.readString()
        fields["YoozooPayNotifyUrl"] = self.readString()
        fields["UnbotifyEnabled"] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20104

    def getMessageVersion(self):
        return self.messageVersion