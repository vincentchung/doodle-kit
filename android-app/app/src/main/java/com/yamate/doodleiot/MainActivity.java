package com.yamate.doodleiot;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.util.Log;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ImageView;
import android.widget.ListView;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.appindexing.Thing;
import com.google.android.gms.common.api.GoogleApiClient;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import javax.net.ssl.HttpsURLConnection;

import static com.yamate.doodleiot.JSONclient.json;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    private static final String mServerURL="http://192.168.50.57:8080";
    ListView lv;

    ArrayList prgmName;
    public static int[] prgmImages = {R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send, R.drawable.ic_menu_send};
    public static String[] prgmNameList = {"Let Us C", "c++", "JAVA", "Jsp", "Microsoft .Net", "Android", "PHP", "Jquery", "JavaScript"};
    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Reloading....", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();

                new JSONclientTask().execute("url",mServerURL+"/skillkit");
            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        new DownloadImageTask((ImageView) findViewById(R.id.imageViewOriginal))
                .execute(mServerURL+"/images/original_1483976432-9347739.jpg");
        new DownloadImageTask((ImageView) findViewById(R.id.imageViewScanResult))
                .execute("https://vincentcwblog.files.wordpress.com/2017/01/leanring_vb_1483976717-676635.jpg?w=700&h=&crop=1");


        lv = (ListView) findViewById(R.id.listView);
        lv.setAdapter(new CustomAdapter(this, prgmNameList, prgmImages));
        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    private Drawable loadImageFromURL(String url) {
        try {
            InputStream is = (InputStream) new URL(url).getContent();
            Drawable draw = Drawable.createFromStream(is, "src");
            return draw;
        } catch (Exception e) {
            //TODO handle error
            Log.i("loadingImg", e.toString());
            return null;
        }
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    public Action getIndexApiAction() {
        Thing object = new Thing.Builder()
                .setName("Main Page") // TODO: Define a title for the content shown.
                // TODO: Make sure this auto-generated URL is correct.
                .setUrl(Uri.parse("http://[ENTER-YOUR-URL-HERE]"))
                .build();
        return new Action.Builder(Action.TYPE_VIEW)
                .setObject(object)
                .setActionStatus(Action.STATUS_TYPE_COMPLETED)
                .build();
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        AppIndex.AppIndexApi.start(client, getIndexApiAction());
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        AppIndex.AppIndexApi.end(client, getIndexApiAction());
        client.disconnect();
    }

    //http request get JSON from server side
    public class JSONclientTask extends AsyncTask<String, Integer, Integer> {
        JSONclient jParser;
        JSONObject json;

        //================================================================
        //execute("http://10.0.2.2:80/TEST/TEST.aspx")\
        //doInBackground(String... param)代表傳入的值可以帶入很多個參數 如:new Item2_AT().execute("1","2");
        protected Integer doInBackground(String... param) {
            int Judge;
            //get Data 單存取資料
            if (param[0].equals("url") == true) {
                // Creating JSON Parser instance
                jParser = new JSONclient();
                // getting JSON string from URL
                json = jParser.getJSONFromUrl(param[1]);
            } else if (param[0].equals("select") == true) {
                String urlParameters = "0";
                urlParameters = "";
                Judge = 1;
                if (Judge == 1) {
                    // Creating JSON Parser instance
                    jParser = new JSONclient();
                    //param[1] 儲存的是url網址
                    json = jParser.makeHttpRequest(param[1], "POST", urlParameters);
                }
            }
            return null;
        }
        protected void onPostExecute(Integer result) {
            //此method是在doInBackground完成以後，才會呼叫的
            super.onPostExecute(result);
            //show Data

            //Log.d("doodle",json.toString());
        }
        //=============================================================
    }

}
