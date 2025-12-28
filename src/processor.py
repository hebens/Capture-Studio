import cv2
import imageio
import pyautogui
from moviepy import ImageSequenceClip
#from moviepy.video.fx.Resize import Resize # Falls wir skalieren wollen
import os

class VideoProcessor:
    @staticmethod
    def save_as_mp4(frames, full_path, fps=30):
        """Konvertiert Frames in eine MP4-Datei mit H.264 Codec."""
        if not frames:
            return
        
        # Dimensionen des ersten Frames bestimmen
        height, width, layers = frames[0].shape
        size = (width, height)
        
        # 'mp4v' oder 'avc1' (H.264) Codec
        # Windows/macOS Kompatibilität: 'mp4v' ist meist am sichersten ohne extra Codecs
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        
        out = cv2.VideoWriter(full_path, fourcc, fps, size)
        
        try:
            for frame in frames:
                # Zur Sicherheit: Resize auf die Header-Größe, falls mss variiert
                if (frame.shape[1], frame.shape[0]) != size:
                    frame = cv2.resize(frame, size)
                # WICHTIG: OpenCV erwartet BGR, unsere Frames sind RGB
                bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                out.write(bgr_frame)
            print(f"MP4 erfolgreich gespeichert: {full_path}")
        except Exception as e:
            print(f"Fehler beim OpenCV-Writing: {e}")
        finally:
            out.release()

    @staticmethod
    def save_as_gif(frames, filename, fps=30):
        """Konvertiert Frames in ein optimiertes GIF."""
        if not frames:
            return
        clip = ImageSequenceClip(frames, fps=fps)
        
        # Wir nutzen imageio mit der 'PIL' engine für bessere GIF-Optimierung
        # 'palettesize' reduziert die Farben auf 256, um Speicher zu sparen
        imageio.mimsave(
            f"{filename}.gif", 
            frames, 
            fps=fps, 
            opt="palette", 
            subrectangles=True
        )
        try:
            # MoviePy 2.x hat verbesserte GIF-Methoden
            clip.write_gif(f"{filename}.gif", fps=fps, opt="None", loop=0)
        finally:
            clip.close() # Wichtig, um RAM sofort freizugeben
        