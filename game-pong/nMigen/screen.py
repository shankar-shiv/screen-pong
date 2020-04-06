
# Syncronism and data from 800x600@72Hz
class screen:
        # VGA parameters.
        width        = 800
        height       = 600
        activeHvideo = width                    # Width of visible pixels.
        activeVvideo = height                   # Height of visible lines.
        hfp          = 56                       # Horizontal front porch length.
        hpulse       = 120                      # Hsync pulse length.
        hbp          = 64                       # Horizontal back porch length.
        vfp          = 37                       # Vertical front porch length.
        vpulse       = 6                        # Vsync pulse length.
        vbp          = 23                       # Vertical back porch length.
        blackH       = hfp + hpulse + hbp       # Hide pixels in one line.
        blackV       = vfp + vpulse + vbp       # Hide lines in one frame.
        hpixels      = blackH + activeHvideo    # Total horizontal pixels.
        vlines       = blackV + activeVvideo    # Total lines.

        # Dimensions.
        wline        = 10                       # Width line of court.
        size_ball    = 10                       # Size ball.

