package com.roundG0929.hibike.api.server.fuction;

import android.app.Activity;
import android.net.Uri;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.roundG0929.hibike.R;

public class ImageApi extends Activity{
    String profileImageUrl = "http://10.0.2.2:5000/api/auth/image/";
    String ridingImageUrl = "http://10.0.2.2:5000/api/auth/rimage/";
    String dangerImageUrl = "http://10.0.2.2:5000/api/board/dimage/";

    public String getProfileImageUrl(String id) {
        return this.profileImageUrl+id;
    }
    public String getRidingImageUrl(String uniqueId) {
        return this.ridingImageUrl+uniqueId;
    }
    public String getDangerImageUrl(String filename) {
        return dangerImageUrl+filename;
    }

    public void setImageOnImageView(Activity activity, ImageView imageView, String imageUri) {
//        Glide.with(activity)
//                .load(imageUri)
//                .disallowHardwareConfig()
//                .into(imageView);
        Glide.with(activity).load(imageUri).error(R.drawable.cyclist).into(imageView);
    }
}
