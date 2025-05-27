from pytubefix import YouTube
import os, re, subprocess

def Download_Song( song_url ):
    print( "-" * 110 )
    print( f">>> Processing: { song_url }" )

    yt = YouTube( song_url )

    song_title = yt.title
    safe_song_title = re.sub( r'[\\/*?:"<>|]', "", song_title )
    song_input_file_name = f"{ safe_song_title }.m4a"
    song_output_file_name = f"{ safe_song_title }.mp3"
    song_output_file_name = re.sub( r"\ ", "_", song_output_file_name )

    if os.path.exists( song_output_file_name ):
        print( f"Song { safe_song_title } is already downloaded - skipping!", "\n", "-" * 110, "\n" )
        return

    print( f">>> Downloading: { song_input_file_name }" )
    try:
        audio_stream = yt.streams.filter( only_audio = True ).order_by( "abr" ).desc().first()
        audio_stream.download( output_path = ".", filename = song_input_file_name )
    except Exception as e:
        print( f"Error downloading { song_input_file_name }: { e }" )
        return

    print( f">>> Converting from .m4a format to .mp3 format" )
    subprocess.run( [ "ffmpeg", "-loglevel", "quiet", "-i", song_input_file_name, "-codec:a", "libmp3lame", 
                      "-qscale:a", "2", song_output_file_name ] )

    print( f">>> Removing .m4a file: { song_input_file_name }" )
    subprocess.run( [ "rm", song_input_file_name ] )

    print( f"Downloaded { song_output_file_name }" )
    print( "-" * 110 )
    print()

YouTube_videos_URLs = [ 
    "https://www.youtube.com/watch?v=gsCUyH0eX9g",
    "https://www.youtube.com/watch?v=ozOpzPWmzHA",
    "https://www.youtube.com/watch?v=3fzUFel786M",
    "https://www.youtube.com/watch?v=qJUGjZHYaM4",
    "https://www.youtube.com/watch?v=_csSTvVmHUw",
    "https://www.youtube.com/watch?v=xlRCHCA0IQc",
    "https://www.youtube.com/watch?v=S9f13Cw2t0M",
    "https://www.youtube.com/watch?v=_cd-2S4ACSg",
    "https://www.youtube.com/watch?v=5eUYYU4CE90",
    "https://www.youtube.com/watch?v=ED2EgbsDXDc",
    "https://www.youtube.com/watch?v=_JEo5WmwJcA",
    "https://www.youtube.com/watch?v=t4fRifhqTOU",
    "https://www.youtube.com/watch?v=RIxjaXsXkoI",
    "https://www.youtube.com/watch?v=Mme8783ghjI",
    "https://www.youtube.com/watch?v=J0GSjOEHif4",
    "https://www.youtube.com/watch?v=2nQ8rmu5ZFU",
    "https://www.youtube.com/watch?v=6hDACW8eRrg",
    "https://www.youtube.com/watch?v=MKgMjcJqCrI",
    "https://www.youtube.com/watch?v=rldu89_A3K4",
    "https://www.youtube.com/watch?v=LmxlM2kWWKk",
    "https://www.youtube.com/watch?v=h28GnkBarfQ",
    "https://www.youtube.com/watch?v=8tw4qdr3Zbo",
    "https://www.youtube.com/watch?v=SRjep36D3lQ",
    "https://www.youtube.com/watch?v=AVO_DWuUU3k",
    "https://www.youtube.com/watch?v=rnFdQ4TId64",
    "https://www.youtube.com/watch?v=9nvpGqS9BH8",
    "https://www.youtube.com/watch?v=wyHIvAIi3fY",
    "https://www.youtube.com/watch?v=wyHIvAIi3fY",
    "https://www.youtube.com/watch?v=wyHIvAIi3fY",
    "https://www.youtube.com/watch?v=0rQaQ2m5kUQ",
    "https://www.youtube.com/watch?v=x53bLddbojk",
    "https://www.youtube.com/watch?v=UorUj8LNru8",
    "https://www.youtube.com/watch?v=mes3BQIKbuo",
    "https://www.youtube.com/watch?v=XoFczLkq0VA",
    "https://www.youtube.com/watch?v=vvfW92cmAbs",
    "https://www.youtube.com/watch?v=T3bYDUYHPtg",
    "https://www.youtube.com/watch?v=HhMOfmilpdY",
    "https://www.youtube.com/watch?v=-FbDvI-Efdc",
    "https://www.youtube.com/watch?v=uyI_aKulc_Y",
    "https://www.youtube.com/watch?v=2-hWiBxhJ7I",
    "https://www.youtube.com/watch?v=ZVTHr-35Dn8",
    "https://www.youtube.com/watch?v=nzIXiYoNO3E",
    "https://www.youtube.com/watch?v=yM7cS7_iO8w",
    "https://www.youtube.com/watch?v=abXhEOZ0fr8",
    "https://www.youtube.com/watch?v=-9T6VKuvIvw",
    "https://www.youtube.com/watch?v=dSqQkqqq8fM",
    "https://www.youtube.com/watch?v=4HPOIbCLml4",
    "https://www.youtube.com/watch?v=wV1jFlAF0YI",
    "https://www.youtube.com/watch?v=dnnKH3daFCE",
    "https://www.youtube.com/watch?v=_XadMyEeo1c",
    "https://www.youtube.com/watch?v=_XadMyEeo1c",
    "https://www.youtube.com/watch?v=QUT1nfU08YE",
    "https://www.youtube.com/watch?v=n66FGCYtWBc",
    "https://www.youtube.com/watch?v=6n2A1mqWL8Y",
    "https://www.youtube.com/watch?v=qFcKvldEbQo",
    "https://www.youtube.com/watch?v=thjntnbToq8",
    "https://www.youtube.com/watch?v=PkVDfG4SYn4",
    "https://www.youtube.com/watch?v=VzwmcbrLv7Y",
    "https://www.youtube.com/watch?v=NsrNZSj_pi4",
    "https://www.youtube.com/watch?v=DjbsrvFF8Mo",
    "https://www.youtube.com/watch?v=bPRCdOKFHr4",
    "https://www.youtube.com/watch?v=bPRCdOKFHr4",
    "https://www.youtube.com/watch?v=1BiCTrJEWhI",
    "https://www.youtube.com/watch?v=t_IC-XBvK0I",
    "https://www.youtube.com/watch?v=d72iyzlxh94",
    "https://www.youtube.com/watch?v=1L0Q7JOF_bA",
    "https://www.youtube.com/watch?v=Zpow4RazeKU",
    "https://www.youtube.com/watch?v=rReHgY8IL1s",
    "https://www.youtube.com/watch?v=IvloHsmi_vg",
    "https://www.youtube.com/watch?v=_0_WAc-Omg8",
    "https://www.youtube.com/watch?v=_0_WAc-Omg8",
    "https://www.youtube.com/watch?v=HEx_ib2ZVs0",
    "https://www.youtube.com/watch?v=iYMkhLofqDE",
    "https://www.youtube.com/watch?v=jn489NMK7Aw",
    "https://www.youtube.com/watch?v=oRdxUFDoQe0",
    "https://www.youtube.com/watch?v=QNJL6nfu__Q",
    "https://www.youtube.com/watch?v=Aw1CQUMp-Gk",
    "https://www.youtube.com/watch?v=Uae2ae9SpmE",
    "https://www.youtube.com/watch?v=vGOlQ08N8Gc",
    "https://www.youtube.com/watch?v=7bM0Kwnhopw",
    "https://www.youtube.com/watch?v=I4FbBrHPXbc",
    "https://www.youtube.com/watch?v=F1yzaPPUBio",
    "https://www.youtube.com/watch?v=FD3UN6dELZg",
    "https://www.youtube.com/watch?v=u1o58ST-tns",
    "https://www.youtube.com/watch?v=O-C2QsMecSA",
    "https://www.youtube.com/watch?v=MUjMFYEdtgg",
    "https://www.youtube.com/watch?v=2HssCWBRc-s",
    "https://www.youtube.com/watch?v=uHwSXV9t_3o",
    "https://www.youtube.com/watch?v=tSm9p7uIdPY",
    "https://www.youtube.com/watch?v=PjYRNaAucg8",
    "https://www.youtube.com/watch?v=1yulsPbvXlc",
    "https://www.youtube.com/watch?v=rngHbUVYdXg",
    "https://www.youtube.com/watch?v=WnKnR-genjI",
    "https://www.youtube.com/watch?v=jSMgYJKLJgw",
    "https://www.youtube.com/watch?v=yGmj0J5uhOI",
    "https://www.youtube.com/watch?v=XB0skcevRF4",
    "https://www.youtube.com/watch?v=Fse8kODwtOM",
    "https://www.youtube.com/watch?v=qwnSAPl2wl0",
    "https://www.youtube.com/watch?v=y-e2hIpFjQM",
    "https://www.youtube.com/watch?v=kvHEy0p5to4",
    "https://www.youtube.com/watch?v=M3ecud1gY5Q",
    "https://www.youtube.com/watch?v=0S0-3g7HhsE",
    "https://www.youtube.com/watch?v=YL0nsoOrK5I",
    "https://www.youtube.com/watch?v=lQRwYZuGn3c",
    "https://www.youtube.com/watch?v=EQLzeR4Mb7A",
    "https://www.youtube.com/watch?v=RHS80xo4PDU",
    "https://www.youtube.com/watch?v=ulUn4CTsjhU",
    "https://www.youtube.com/watch?v=g-YQ7w2aUn8",
    "https://www.youtube.com/watch?v=OrDPtCnbi9I",
    "https://www.youtube.com/watch?v=vG2UTYhxrwU",
    "https://www.youtube.com/watch?v=gYOBcsqQNOE",
    "https://www.youtube.com/watch?v=ygk__Cr93yM",
    "https://www.youtube.com/watch?v=zFiKf4OA_gY",
    "https://www.youtube.com/watch?v=zFiKf4OA_gY",
    "https://www.youtube.com/watch?v=pRpeEdMmmQ0",
    "https://www.youtube.com/watch?v=X77aaOKOn_s",
    "https://www.youtube.com/watch?v=QbE2mLrK1LM",
    "https://www.youtube.com/watch?v=LQLuoZRn7xE",
    "https://www.youtube.com/watch?v=EoLtocWfwPw",
    "https://www.youtube.com/watch?v=4XCq-5FcjIM",
    "https://www.youtube.com/watch?v=ELAh_MjMOio",
    "https://www.youtube.com/watch?v=npVX9zdhTNw",
    "https://www.youtube.com/watch?v=ulfEWCPvu6E",
    "https://www.youtube.com/watch?v=t37ieNxQ9Q8",
    "https://www.youtube.com/watch?v=qM-TJg4cHHU",
    "https://www.youtube.com/watch?v=Uj_18hXo5G0",
    "https://www.youtube.com/watch?v=PbtcchWTn28",
    "https://www.youtube.com/watch?v=ok4mZ_yuwko",
    "https://www.youtube.com/watch?v=VFp3eqz6RT0",
    "https://www.youtube.com/watch?v=lYv3FuYPoQY",
    "https://www.youtube.com/watch?v=bdiZZtr8-HA",
    "https://www.youtube.com/watch?v=pn1nlkHMxbk",
    "https://www.youtube.com/watch?v=Nww0bh4yX3I",
    "https://www.youtube.com/watch?v=a8zRxwl0-3k",
    "https://www.youtube.com/watch?v=a8zRxwl0-3k",
    "https://www.youtube.com/watch?v=roqXbkFOeio",
    "https://www.youtube.com/watch?v=iaNgco2oRUs",
    "https://www.youtube.com/watch?v=i4auYHXqWrk",
    "https://www.youtube.com/watch?v=tmjDyxbfaZU",
    "https://www.youtube.com/watch?v=r4_Ob3MxXd0",
    "https://www.youtube.com/watch?v=BthWzOAihkk",
    "https://www.youtube.com/watch?v=QIJje6xGWJg",
    "https://www.youtube.com/watch?v=MFgEj07lntA",
    "https://www.youtube.com/watch?v=tGXnuFu2LHU"
]

for index, song_url in enumerate( YouTube_videos_URLs ):
    print( f"\n>>> Progress: { index + 1 } / { len( YouTube_videos_URLs ) }" )
    Download_Song( song_url )

print( "All songs downloaded and converted to MP3 format." )