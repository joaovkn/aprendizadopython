//basic/models/UserForm.php

<?php

namespace app\models;

use yii\base\Model;

class UserForm extends Model{

    public $name;
    public $email;

    public function rules(){

        return [
        [['name','email'], 'required'],
        ['email', 'email'],
        ];
    }

}


//basic/views/site

<?php

use yii\helpers\Html;
use yii\widgets\ActiveForm;
?>

<?php
    if(Yii::$app->session->hasFlash('success')){
        echo Yii::$app->session->getFlash('success');
    }
?>

<?php $form = ActiveForm::begin(); ?>
<?= $form->field($model,'name'); ?>
<?= $form->field($model,'email'); ?>

<?= Html::submitButton('Submit',['class'=>'btn btn-success']); ?>
