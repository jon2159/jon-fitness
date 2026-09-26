// Tiny UI helper for the Daily Pump macOS window (iOS app running on Apple Silicon).
// Commands (screen coordinates in points; the caller converts window-relative -> screen):
//   dpui window                 -> prints "id x y w h" of the DailyPump window (on screen), exit 1 if none
//   dpui click X Y              -> left click at screen point
//   dpui scroll X Y DY          -> scroll wheel at screen point by DY pixels (negative = content moves up)
// Needs Accessibility permission for the calling app (granted by the user). Touches nothing but the pointer/wheel.
import Cocoa

func windowInfo() -> (Int, CGRect)? {
    let list = CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]] ?? []
    for w in list where (w[kCGWindowOwnerName as String] as? String) == "DailyPump" {
        if let b = w[kCGWindowBounds as String] as? [String: Any], let id = w[kCGWindowNumber as String] as? Int {
            let r = CGRect(x: (b["X"] as? CGFloat) ?? 0, y: (b["Y"] as? CGFloat) ?? 0,
                           width: (b["Width"] as? CGFloat) ?? 0, height: (b["Height"] as? CGFloat) ?? 0)
            if r.width > 100 { return (id, r) }
        }
    }
    return nil
}

let a = CommandLine.arguments
guard a.count >= 2 else { print("usage: dpui window|click X Y|scroll X Y DY"); exit(2) }
switch a[1] {
case "window":
    if let (id, r) = windowInfo() { print("\(id) \(Int(r.origin.x)) \(Int(r.origin.y)) \(Int(r.width)) \(Int(r.height))") } else { exit(1) }
case "click":
    let p = CGPoint(x: Double(a[2])!, y: Double(a[3])!)
    for t in [CGEventType.leftMouseDown, .leftMouseUp] {
        CGEvent(mouseEventSource: nil, mouseType: t, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
        usleep(60_000)
    }
case "scroll":
    let p = CGPoint(x: Double(a[2])!, y: Double(a[3])!)
    CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
    usleep(80_000)
    let dy = Int32(a[4])!
    CGEvent(scrollWheelEvent2Source: nil, units: .pixel, wheelCount: 1, wheel1: dy, wheel2: 0, wheel3: 0)?.post(tap: .cghidEventTap)
default: exit(2)
}
