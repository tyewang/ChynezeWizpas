function translate(){
    var sourceText = jQuery('#sourceText').val();
    jQuery.ajax({
        type: "Get",
        url: "translator/translate",
        data: {sourceText: sourceText},
        beforeSend: function() {
            jQuery('#translatedTextBlock').hide();
            jQuery('#loaderTextBlock').show();
         },
         complete: function(){
            jQuery('#loaderTextBlock').hide();
            jQuery('#translatedTextBlock').show();
         }})
        .done(updateTranslatedText);
}

function updateTranslatedText(translatedText){
    jQuery('#translatedText').text(translatedText);
}

jQuery(document).ready(function(){
    jQuery('#loaderTextBlock').hide();
    jQuery('#translateButton').click(translate);
})
