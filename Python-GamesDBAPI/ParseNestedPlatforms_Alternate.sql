DECLARE @json NVarChar(max) = N'{
            "25": {
                "id": 25,
                "name": "3DO",
                "alias": "3do",
                "icon": "3do-1336524121.png",
                "console": "25.png",
                "controller": null,
                "developer": "The 3DO Company",
                "manufacturer": "Panasonic",
                "media": "Disc",
                "cpu": "32-bit 12.5 MHz RISC CPU (ARM60)",
                "memory": "2 MB of main RAM",
                "graphics": null,
                "sound": "16-bit stereo sound",
                "maxcontrollers": "1",
                "display": "640×480",
                "overview": "The 3DO Interactive Multiplayer, often called simply 3DO, is a video game console originally produced by Panasonic in 1993. Further renditions of the hardware were released in 1994 by Sanyo and Goldstar. The consoles were manufactured according to specifications created by The 3DO Company, and were originally designed by Dave Needle and RJ Mical of New Technology Group. The system was conceived by entrepreneur and Electronic Arts founder Trip Hawkins.\r\n\r\nDespite a highly promoted launch (including being named Time magazine&#039;s \"1994 Product of the Year\") and a host of cutting-edge technologies, the 3DO&#039;s high price (US$699.95 at launch), limited third-party developer support, and an over-saturated console market prevented the system from achieving success comparable to competitors Sega and Nintendo.  This console was released in North America on October 4, 1993, Japan on March 20, 1994 and in Europe in 1994.",
                "youtube": "1Jq8tFmaXbY"
            },
            "4944": {
                "id": 4944,
                "name": "Acorn Archimedes",
                "alias": "acorn-archimedes",
                "icon": "acorn-archimedes-1446690349.png",
                "console": "4944.png",
                "controller": null,
                "developer": "Acorn Computers",
                "manufacturer": "Acorn Computers",
                "media": null,
                "cpu": "Acorn RISC Machine",
                "memory": "512 KB ~ 16 MB",
                "graphics": null,
                "sound": null,
                "maxcontrollers": null,
                "display": null,
                "overview": "The Acorn Archimedes is a family of personal computers designed by Acorn Computers Ltd in Cambridge, England and sold in the late-1980s to mid-1990s, their first general purpose home computer based on their own ARM architecture. The Archimedes was one of the most powerful home computers available during the late 1980s and early 1990s; its main CPU was faster than the Motorola 68000 microprocessors found in the more popular Commodore Amiga and Atari ST machines.",
                "youtube": null
            }
        }';
 
SELECT A.[Key],B.* 
FROM OpenJson(@json) as A
OUTER APPLY OPENJSON(A.[Value]) 
						WITH([id] INT,
                             [name] NVARCHAR(50),
							 alias NVARCHAR(50),
							 icon NVARCHAR(100),
							 console NVARCHAR(100),
							 controller NVARCHAR(100),
							 developer NVARCHAR(100),
							 manufacturer NVARCHAR(100),
							 media NVARCHAR(250),
							 cpu NVARCHAR(250),
							 memory NVARCHAR(250),
							 graphics NVARCHAR(250),
							 sound NVARCHAR(50),
							 maxcontrollers INT,
							 display NVARCHAR(250),
							 overview NVARCHAR(Max)
							 )B 
 