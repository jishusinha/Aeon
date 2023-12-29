from bot import CMD_SUFFIX

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'esshu{CMD_SUFFIX}', f'es{CMD_SUFFIX}']
        self.YtdlCommand = [f'abhi{CMD_SUFFIX}', f'ab{CMD_SUFFIX}']
        self.LeechCommand = [f'upload{CMD_SUFFIX}', f'u{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdl{CMD_SUFFIX}', f'y{CMD_SUFFIX}']
        self.CloneCommand = [f'kishu{CMD_SUFFIX}', f'ki{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'ishu{CMD_SUFFIX}'
        self.StopAllCommand = [f'stopall{CMD_SUFFIX}', 'stopallbot']
        self.ListCommand = f'sizuka{CMD_SUFFIX}'
        self.SearchCommand = f'sakura{CMD_SUFFIX}'
        self.StatusCommand = [f'status{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = f'authorize{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', 'pingall']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', 'statsall']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting{CMD_SUFFIX}'
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.SpeedCommand = f'speedtest{CMD_SUFFIX}'
        self.RssCommand = f'kakashi{CMD_SUFFIX}'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.MediaInfoCommand = f'mediainfo{CMD_SUFFIX}'
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', 'broadcastall']

BotCommands = _BotCommands()
