//
//  escryptor.h
//  Eggshell OSX Payload
//
//  Created by Lucas Jackson on 2/26/17.
//  Copyright © 2017 Lucas Jackson. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface escryptor : NSObject
+(NSString *)encryptNSStringToB64:(NSString*)str :(NSString*)data;
+(NSString *)decryptB64ToNSString:(NSString*)str :(NSString*)data;
@end